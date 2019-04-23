from plumbum import local

print(local.path(__file__).dirname.up())
