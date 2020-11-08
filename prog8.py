samochody = ['syrena', 'polonez']
pojemnosci = [1.0, 1.4]
#
# print (samochody[0])
# print (samochody[1])
# # print (samochody[2])
#
# # print("petla 1")
# # for s in samochody:
# #     print(s)
#
# print("== petla 2 po indexie ===")
# print("len: {0}" .format(len(samochody)))
# print("range: {0}" .format(range(2)))
#
# # print ("==petla 1 po indexie ===")
# # for idx in range(len(samochody)):
# #     print ("{0} {1}" .format(idx, samochody[idx]))


# zoo = ['zyrafa', 'slonie', 'malp']
# ilosc = [1, 3, 6]
#
# for idx in range(len(zoo)):
#     print("W zoo jest {0} - {1}" .format(ilosc[idx], zoo[idx]))

print("== listy ->string ==")
print(",".join(samochody))

print("==string -> lista ==")
import_samochody = "kia,mercedes,nissan".split(',')
print(import_samochody)
