#!-*-coding:utf-8-*-
def quantity_happy_kids(greed, cookies):
    greed.sort()
    cookies.sort()
    result = 0
    for i in greed:
        if len(cookies) > 0:
            for j in cookies:
                cookies.pop(0)
                if j >= i:
                    result += 1
                    break
    return result


if __name__ == "__main__":
    kids_count = 10
    greed_list = [8, 5, 5, 8, 6, 9, 8, 2, 4, 7]
    cookies_count = 8
    cookies_size = [9, 8, 1, 1, 1, 5, 10, 8]
    print(quantity_happy_kids(greed_list, cookies_size))


