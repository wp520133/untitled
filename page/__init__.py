from selenium.webdriver.common.by import By

url = "http://192.168.102.30/"

# 点击登录
login_click = By.CSS_SELECTOR, "li.item:nth-child(7) > a:nth-child(1)"
# 输入用户名
login_username =By.CSS_SELECTOR, "#user_name"
# 输入密码
login_password = By.CSS_SELECTOR, "#user_password"
# 输入验证码
login_captcha_code = By.CSS_SELECTOR, "#captcha_code"
# 点击登录
login_button = By.CSS_SELECTOR, "#login_form > div:nth-child(5) > div > button.btn.btn-primary"
# 点击退出
login_out=By.CSS_SELECTOR,"#shop_header > div.span7.shop_header_right > ul > li:nth-child(7) > a:nth-child(2)"