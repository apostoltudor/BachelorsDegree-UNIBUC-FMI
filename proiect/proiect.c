#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/wait.h>

//permuta un cuvant
void permute(char *word, char *perm, int length) {
    for (int i = 0; i < length; i++) perm[i] = i;
    for (int i = length - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        char temp = perm[i];
        perm[i] = perm[j];
        perm[j] = temp;
    }
    char temp[length];
    for (int i = 0; i < length; i++) temp[i] = word[perm[i]];
    memcpy(word, temp, length);
}

//inverseaza permutarea
void reverse_permute(char *word, char *perm, int length) {
    char temp[length];
    for (int i = 0; i < length; i++) temp[perm[i]] = word[i];
    memcpy(word, temp, length);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_file> [perm_file]\n", argv[0]);
        return 1;
    }

    //dechide input.txt
    int fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        perror("Failed to open input file");
        return 1;
    }

    //mapeaza input.txt in memorie
    off_t size = lseek(fd, 0, SEEK_END);
    lseek(fd, 0, SEEK_SET);
    char *data = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0);
    close(fd);

    if (!data) {
        perror("Failed to mmap file");
        return 1;
    }

    if (argc == 2) {
        //criptarea
        FILE *perm_file = fopen("permutations.txt", "w");
        if (!perm_file) {
            perror("Failed to create permutations file");
            return 1;
        }

        FILE *output = fopen("output.txt", "w");
        if (!output) {
            perror("Failed to create output file");
            fclose(perm_file);
            return 1;
        }

        char *word = strtok(data, " \n");
        while (word) {
            int length = strlen(word);
            char perm[length];

            pid_t pid = fork();
            if (pid == 0) { 
                permute(word, perm, length);
                fwrite(perm, sizeof(char), length, perm_file); 
                fprintf(output, "%s ", word);                  
                exit(0); 
            } else if (pid < 0) {
                perror("Failed to fork");
                return 1;
            }

            word = strtok(NULL, " \n");
        }

        while (wait(NULL) > 0);

        fclose(perm_file);
        fclose(output);
    } else if (argc == 3) {
        //decriptare
        FILE *perm_file = fopen(argv[2], "r");
        if (!perm_file) {
            perror("Failed to open permutations file");
            return 1;
        }

        FILE *output = fopen("decrypted.txt", "w");
        if (!output) {
            perror("Failed to create decrypted file");
            fclose(perm_file);
            return 1;
        }

        char *word = strtok(data, " \n");
        while (word) {
            int length = strlen(word);
            char perm[length];
            fread(perm, sizeof(char), length, perm_file); 
            reverse_permute(word, perm, length);  
            fprintf(output, "%s ", word);      
            word = strtok(NULL, " \n");
        }

        fclose(perm_file);
        fclose(output);
    }

    munmap(data, size);
    return 0;
}
