from config.filter_keyword import filter_string
# using datetime module
import datetime
import os

def get_timestamp() -> str:
    # ct stores current time
    ct = datetime.datetime.now()
    print("current time:-", ct)
    
    # ts store timestamp of current time
    ts = ct.timestamp()
    return str(int(ts))

class ShoppingOnlineLocation:
    def __init__(self, location: str, keyword: str, keyword1: str, keyword2: str, keyword3: str, page: str) -> None:
        self.location = location
        self.keyword = keyword
        self.keyword1 = keyword1
        self.keyword2 = keyword2
        self.keyword3 = keyword3

        self.page = page
        
    def get_base_url(self) -> str:
        match self.location:
            case "tiki":
                filter_keyword = filter_string(self.keyword, "%20")
                base_url = "https://tiki.vn/search?q={0}&page={1}".format(filter_keyword, self.page)
                return base_url
            case "shopee":
                filter_keyword = filter_string(self.keyword, "%20")
                base_url = "https://shopee.vn/search?keyword={0}&page={1}".format(filter_keyword, self.page)
                return base_url
            case "lazada":
                filter_keyword = filter_string(self.keyword, "-")
                base_url = "https://www.lazada.vn/tag/{0}/?page={1}".format(filter_keyword, self.page)
                return base_url
            case "amazon":
                filter_keyword = filter_string(self.keyword, "+")
                base_url = "https://www.amazon.com/s?k={0}&page={1}".format(filter_keyword, self.page)
                return base_url
            case "fahasa":
                filter_keyword = filter_string(self.keyword, "+")
                base_url = "https://www.fahasa.com/{0}/{1}/{2}/{3}.html?order=num_orders&limit=1000&p={4}".format(self.keyword,self.keyword1,self.keyword2, self.keyword3, self.page)
                return base_url
            case default:
                return "we cannot support this"

    # def add_product_to_csv(self, products):
    #     ts = get_timestamp()
    #     with open(
    #         './{0}/product_info_in_{1}_{2}.csv'.format("csv", self.location, ts), 
    #         "a", encoding="utf-8") as f:
    #         for item in products:
    #             f.write(item)
    def add_product_to_csv(self, products):
        ts = get_timestamp()
        csv_file_path = './{0}/{1}/product_info_in_{2}_{3}_{4}_{5}.csv'.format("csv", self.keyword.replace("-","_"), self.keyword1.replace("-",""), self.keyword2.replace("-",""), self.keyword3.replace("-",""), self.page)
        
        # Kiểm tra xem tệp có dữ liệu hay không
        is_file_empty = not os.path.isfile(csv_file_path) or os.path.getsize(csv_file_path) == 0
        
        with open(csv_file_path, "a", encoding="utf-8") as f:
            # Chỉ ghi tên cột nếu tệp là trống
            if is_file_empty:
                f.write("Href, ImageUrl, Title, Rating, NumRatings, DataSupplier, DataAuthor, DataPublisher, DataPublishYear, DataSize, DataBookLayout, Des, DataQtyOfPage, Cate0, Cate1, Cate2, Cate3, PriceSpecial, PriceOld\n")
            
            for item in products:
                f.write(item)