# Use an i386-based Ubuntu image (32-bit)
FROM i386/ubuntu:20.04

# Install nasm (assembler) and gcc (compiler and linker)
RUN apt-get update && apt-get install -y gcc libc6-dev g++-multilib gdb

# Set a working directory for your assembly code
WORKDIR /app
