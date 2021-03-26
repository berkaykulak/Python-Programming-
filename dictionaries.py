
sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

print(sozluk)


len(sozluk)

sozluk = {"REG": 10,
          "LOJ": 20,
          "CART": 30}

print(sozluk)

sozluk = {"REG": ["RMSE", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}

print(sozluk)

# Sozluk Eleman Islemleri

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

print(sozluk[0])
print(sozluk["REG"])
print(sozluk["LOJ"])




sozluk = {"REG": ["RMSE", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}

print(sozluk["REG"])


sozluk = {"REG": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},

          "LOJ": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},

          "CART": {"RMSE": 10,
                   "MSE": 20,
                   "SSE": 30}}


print(sozluk)
print(sozluk["REG"]["SSE"])



# Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"

print(sozluk)


sozluk["REG"] = "Coklu Dogrusal Regresyon"
print(sozluk)

sozluk[1] = "Yapay Sinir Aglari"

print(sozluk)

l = [1]
print(l)


sozluk[l] = "yeni bir sey"

t = ("tuple",)

sozluk[t] = "yeni bir sey"
print(sozluk)
