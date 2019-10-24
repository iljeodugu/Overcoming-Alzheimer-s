from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://zzzscore.com/1to50/?ts=1571891513692")

result_list = []
number_list = []

for i in range(1,26):
    result = driver.find_elements_by_xpath('//*[@id="grid"]/div[' + str(i) + ']')
    result_list.append(result[0])
    number_list.append(result[0].text)

for i in range(1,26):
    for j in range(25):
        if(number_list[j] == str(i)):
            result_list[j].click()
            break

number_list = []

for i in range(25):
    number_list.append(result_list[i].text)
    print(result_list[i].text)
print(number_list)
for i in range(26,51):
    for j in range(25):
        if(number_list[j] == str(i)):
            result_list[j].click()
            break
