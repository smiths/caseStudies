ifeq "$(OS)" "Windows_NT"
    # WINDOWS
	TARGET_EXTENSION=.exe
	RM=del
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S), Linux)
		# LINUX 
		TARGET_EXTENSION=
		RM=rm
	endif
	ifeq ($(UNAME_S), Darwin)
		# OSX
		TARGET_EXTENSION=
		RM=rm
	endif
endif

C_COMPILER=gcc

CFLAGS = -std=c99

LINKED_LIBS = -lm

SRC_FILES=$(wildcard src/*.c)

PROG_NAME=glassbr
PROG_TARGET=$(PROG_NAME)$(TARGET_EXTENSION)

.PHONY: all
all: prog

.PHONY: prog
prog: $(PROG_TARGET) 
	./$(PROG_TARGET) infile

$(PROG_TARGET):
	$(C_COMPILER) $(CFLAGS) $(SRC_FILES) -o $(PROG_TARGET) $(LINKED_LIBS)

.PHONY: clean
clean:
	@-$(RM) $(PROG_TARGET) outputfile.txt