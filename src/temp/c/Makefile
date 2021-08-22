CC=gcc
CFLAGS=-g 
EXT= # exe, out, or custom
OUTPUT_NAME= # Project Name
SRC = $(patsubst %.c)
HEADERS = $(patsubst %.h)
OUTPUT_DIRECTORY = $(wildcard out)\\$(OUTPUT_NAME).$(EXT)

build: $(HEADERS)
	mkdir Out
	$(CC) $(CFLAGS) $(SRC) -o $(OUTPUT_DIRECTORY)


clean:
	-rm $(wildcard out/*)
