import requests

# def main():
#     word = input('検索キーワード：')
#     requests.get('https://ci.nii.ac.jp/books/opensearch/search?'
#                  'format=json')

# if __name__ == '__main__':
#     main()

res=requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=2260021')

res_json = res.json()
results= res_json['results'][0]
address= results['address1']+results['address2']+results['address3']
print(address)

