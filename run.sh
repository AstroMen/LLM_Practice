#!/bin/sh

# Change into the FFmpeg directory
cd FFmpeg
output_dir="../FFmpeg_so"
mkdir -p "$output_dir"

# Loop through each version and compile it
for version in 'n4.1.10' 'n4.1.1'
do
  # Checkout the specific version
  git checkout "$version"

  # Clean any previous build files
  make clean

  # Configure FFmpeg with the desired options
  CFLAGS="-g" ./configure --enable-shared > log.txt
  make >> log.txt

  # Install the compiled libraries into a separate directory for each version
  make install
  
  find . -name "*.so" -exec cp {} "$output_dir" \;

  # Reset the working directory to the initial state
  git reset --hard
done


