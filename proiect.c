#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <ctype.h>
#include <time.h>

//func care endcripteaza un cuv
void process_word_encrypt(char *input_ptr, char *output_ptr, char *perm_ptr, int length) {
    //ne fol de adresele pointerilor
    char *p = malloc(length);  //facem un vector pt indicii literelor
    for (int i = 0; i < length; i++) p[i] = i;

    //pt o amestecare dif folosim seed de timpul curent xor proc id
    unsigned int seed = time(NULL) ^ getpid();
    for (int i = length - 1; i > 0; i--) {
        int j = rand_r(&seed) % (i + 1);
        char temp = p[i];
        p[i] = p[j];
        p[j] = temp;
    } //permutam vectorul de indici

    //salvam permutarea in permutations.txt
    memcpy(perm_ptr, p, length);

    //punem cuv criptat in output.txt
    for (int i = 0; i < length; i++) {
        output_ptr[i] = input_ptr[p[i]];
    }

    free(p); //eliberam memoria alocata pt vect de indici
}

//func pt decriptare
void process_word_decrypt(char *input_ptr, char *output_ptr, char *perm_ptr, int length) {
    // Reconstituim cuvântul original folosind permutarea salvată
    for (int i = 0; i < length; i++) {
        //ne fol de textul criptat si permutare pt a pune literele la locul lor
        output_ptr[perm_ptr[i]] = input_ptr[i];
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) { //verif sa avem input file
        fprintf(stderr, "Trebuie input file dupa: %s \n", argv[0]);
        return 1;
    }

    const char *input_path = argv[1];
    int mode_encrypt = (argc == 2); //1 = criptare, 0 = decriptare

    //deschidem si citim din input file
    int fd_in = open(input_path, O_RDONLY);
    if (fd_in < 0) { perror("Eroare open input"); return 1; }

    struct stat st;  //luam date despre fisier
    if (fstat(fd_in, &st) < 0) { perror("Eroare fstat"); return 1; }
    off_t fsize = st.st_size; //folosim off_t sa nu dea overflow si salvam marimea fisierului

    if (fsize == 0) {
        printf("Fisierul de intrare este gol.\n");
        return 0;
    }

    char *in_map = mmap(NULL, fsize, PROT_READ, MAP_PRIVATE, fd_in, 0);
    //incarca ce e in input file in memorie si salvam adresa de inceput
    if (in_map == MAP_FAILED) { perror("Eroare mmap input"); return 1; }
    close(fd_in);

    //alegem fisierele in functie de mode_encrypt
    int fd_out, fd_perm;
    char *out_path = mode_encrypt ? "output.txt" : "decrypted.txt";
    char *perm_path = mode_encrypt ? "permutations.txt" : argv[2];

    //deschidem output
    fd_out = open(out_path, O_RDWR | O_CREAT | O_TRUNC, 0666);
    if (fd_out < 0) { perror("Eroare open output"); return 1; }
    
    //steam dimensiunea output sa fie = cu input
    if (ftruncate(fd_out, fsize) < 0) { perror("Eroare ftruncate output"); return 1; }

    //mapam output in memorie
    char *out_map = mmap(NULL, fsize, PROT_READ | PROT_WRITE, MAP_SHARED, fd_out, 0);
    if (out_map == MAP_FAILED) { perror("Eroare mmap output"); return 1; }
    close(fd_out);

    char *perm_map = NULL;
    if (mode_encrypt) { //daca criptam
        fd_perm = open(perm_path, O_RDWR | O_CREAT | O_TRUNC, 0666);
        if (ftruncate(fd_perm, fsize) < 0) { perror("ftruncate perm"); return 1; }
        perm_map = mmap(NULL, fsize, PROT_READ | PROT_WRITE, MAP_SHARED, fd_perm, 0);
    } else { //daca decriptam
        fd_perm = open(perm_path, O_RDONLY); // La decriptare doar citim permutările
        perm_map = mmap(NULL, fsize, PROT_READ, MAP_PRIVATE, fd_perm, 0);
    }
    
    if (fd_perm < 0 || perm_map == MAP_FAILED) { perror("Eroare perm file"); return 1; }
    close(fd_perm);


    //procesarea caracterelor
    int i = 0;
    while (i < fsize) {  //gestionam separatorii
        if (!isalnum(in_map[i])) {  //daca nu e alfanumeric nu il scjimbam
            out_map[i] = in_map[i]; //il copiem cum e
            if (mode_encrypt) perm_map[i] = i;
            i++;
            continue; //skip
        }

        //incepe un cuvant
        int start = i;
        while (i < fsize && isalnum(in_map[i])) {
            i++;
        }
        int len = i - start; //calc lungimea cuv
        
        if (mode_encrypt) {  //doar daca criptam
            pid_t pid = fork();
            if (pid == 0) {
                //procese copil pt criptare
                process_word_encrypt(in_map + start, out_map + start, perm_map + start, len);
                exit(0);
            } else if (pid < 0) {
                perror("Eroare fork");
            }
        } else { //decriptare
            process_word_decrypt(in_map + start, out_map + start, perm_map + start, len);
        }
    }

    //asteptam sa se termine toate procesele copil
    while (wait(NULL) > 0);

    //eliberam memoria mapata
    munmap(in_map, fsize);
    munmap(out_map, fsize);
    munmap(perm_map, fsize);

    printf("Am terminat, vezi: %s\n", out_path);

    return 0;
}