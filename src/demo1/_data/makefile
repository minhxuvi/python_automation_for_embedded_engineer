
GCC = $(if $(GCC_DIR),$(GCC_DIR)/gcc,gcc)

all: main print
main: main.c
	$(GCC) -o main main.c
clean:
	rm -f main

print:
	@echo os=$(os)
	@echo compiler=$(compiler)
	@echo core=$(core)
	@echo PLUGINS_DIR=$(PLUGINS_DIR)
	@echo BUILD_DIR=$(BUILD_DIR)
	@echo GCC_DIR=$(GCC_DIR)
