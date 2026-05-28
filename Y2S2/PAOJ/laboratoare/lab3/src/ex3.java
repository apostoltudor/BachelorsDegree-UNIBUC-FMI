public abstract class ex3 {
    public static class Animal{
        public void makeSound(){

        }
    }

    public static class Dog extends Animal{
        @Override
        public void makeSound(){
            System.out.printf("Woof! ");
        }
    }

    public static class Cat extends Animal{
        @Override
        public void makeSound(){
            System.out.printf("Meow! ");
        }
    }

    public static void main(String[] args) {
        Animal[] animale = new Animal[4];
        animale[0] = new Dog();
        animale[1] = new Cat();
        animale[2] = new Dog();
        animale[3] = new Cat();

        for (Animal a : animale) {
            a.makeSound();
        }

//        ex3 x = new ex3();  nu merge ca e abstract
    }

}
