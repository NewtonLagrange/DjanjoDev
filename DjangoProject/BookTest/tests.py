from django.test import TestCase

# Create your tests here.
a = '123'.encode('gbk')
print(str(a, encoding='gbk'))