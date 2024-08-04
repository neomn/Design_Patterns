class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer specs: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def configure_ram(self, ram):
        self.computer.ram = ram
        return self

    def configure_storage(self, storage):
        self.computer.storage = storage
        return self

    def configure_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer

class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        return self.builder.configure_cpu("Intel i9") \
                           .configure_ram("32GB") \
                           .configure_storage("1TB SSD") \
                           .configure_gpu("NVIDIA RTX 3080") \
                           .build()

    def build_office_pc(self):
        return self.builder.configure_cpu("Intel i5") \
                           .configure_ram("16GB") \
                           .configure_storage("512GB SSD") \
                           .build()

# Usage
builder = ComputerBuilder()
director = Director(builder)

gaming_pc = director.build_gaming_pc()
print(gaming_pc)

office_pc = director.build_office_pc()
print(office_pc)

# Custom build
custom_pc = builder.configure_cpu("AMD Ryzen 7") \
                   .configure_ram("64GB") \
                   .configure_storage("2TB NVMe SSD") \
                   .configure_gpu("AMD Radeon RX 6800 XT") \
                   .build()
print(custom_pc)
