PREFIX       := $(HOME)/torch/install
NVCC_PREFIX  := /usr/local/cuda/bin
CFLAGS       := -I$(PREFIX)/include/THC -I$(PREFIX)/include/TH -I$(PREFIX)/include -I$(HOME)/torch/install/include/ -I$(HOME)/torch/install/include/THC -I$(HOME)/torch/install/include/TH/
LDFLAGS_NVCC := -L$(PREFIX)/lib -Xlinker -rpath,$(PREFIX)/lib -lluaT -lTHC -lTH -lpng

all: libcuda_utils.so 

libcuda_utils.so: cuda_utils.cu
	$(NVCC_PREFIX)/nvcc -arch sm_35 -O3 -DNDEBUG --compiler-options '-fPIC' -o libcuda_utils.so \
    --shared cuda_utils.cu \
    $(CFLAGS) $(LDFLAGS_NVCC) \
    -L/home/gimpei/torch/install/lib/

clean:
	find . -type f | xargs -n 5 touch
	rm -f libcuda_utils.so  
