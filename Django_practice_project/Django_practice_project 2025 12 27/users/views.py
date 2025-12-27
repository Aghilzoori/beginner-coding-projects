# users/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile  # اضافه کردن ایمپورت مدل

# صفحه اصلی لاگین
def login_page(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>ورود به سیستم</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                padding: 40px;
                border-radius: 20px;
                width: 100%;
                max-width: 500px;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
                text-align: center;
            }
            
            h1 {
                color: #2c3e50;
                margin-bottom: 30px;
                font-size: 28px;
            }
            
            .tabs {
                display: flex;
                justify-content: center;
                margin-bottom: 30px;
                border-bottom: 2px solid #eee;
            }
            
            .tab-btn {
                padding: 15px 30px;
                background: none;
                border: none;
                font-size: 18px;
                cursor: pointer;
                color: #666;
                position: relative;
                transition: all 0.3s;
            }
            
            .tab-btn.active {
                color: #3498db;
                font-weight: bold;
            }
            
            .tab-btn.active::after {
                content: '';
                position: absolute;
                bottom: -2px;
                left: 0;
                width: 100%;
                height: 3px;
                background: #3498db;
                border-radius: 3px;
            }
            
            .tab-content {
                display: none;
                text-align: right;
            }
            
            .tab-content.active {
                display: block;
            }
            
            .form-group {
                margin-bottom: 20px;
            }
            
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
                color: #34495e;
            }
            
            input {
                width: 100%;
                padding: 15px;
                border: 2px solid #e0e0e0;
                border-radius: 10px;
                font-size: 16px;
                transition: border 0.3s;
            }
            
            input:focus {
                border-color: #3498db;
                outline: none;
            }
            
            button {
                width: 100%;
                padding: 16px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.3s;
                margin-top: 10px;
            }
            
            button:hover {
                transform: translateY(-2px);
            }
            
            .alert {
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 20px;
                text-align: center;
                font-weight: bold;
                display: none;
            }
            
            .alert.success {
                background: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            
            .alert.error {
                background: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            
            .links {
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #eee;
            }
            
            .link-btn {
                display: block;
                padding: 15px;
                margin: 10px 0;
                background: #f8f9fa;
                color: #2c3e50;
                text-decoration: none;
                border-radius: 10px;
                border: 2px solid #e0e0e0;
                text-align: center;
                font-weight: bold;
                transition: all 0.3s;
            }
            
            .link-btn:hover {
                background: #e9ecef;
                border-color: #3498db;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 سیستم مدیریت کاربران</h1>
            
            <div class="tabs">
                <button class="tab-btn active" onclick="showTab('login')">ورود کاربران</button>
                <button class="tab-btn" onclick="showTab('register')">ثبت نام جدید</button>
            </div>
            
            <div id="message" class="alert"></div>
            
            <!-- تب ورود -->
            <div id="login-tab" class="tab-content active">
                <form id="loginForm">
                    <div class="form-group">
                        <label for="login-username">نام کاربری:</label>
                        <input type="text" id="login-username" 
                               placeholder="نام کاربری خود را وارد کنید" required>
                    </div>
                    
                    <button type="submit">ورود به سیستم</button>
                </form>
                
                <div class="links">
                    <p style="color: #666; margin-bottom: 15px;">کاربر جدید هستید؟</p>
                    <a href="javascript:void(0);" onclick="showTab('register')" class="link-btn">
                        📝 ثبت نام جدید
                    </a>
                </div>
            </div>
            
            <!-- تب ثبت نام -->
            <div id="register-tab" class="tab-content">
                <form id="registerForm">
                    <div class="form-group">
                        <label for="username">نام کاربری *</label>
                        <input type="text" id="username" name="username" required>
                        <small style="color: #666; display: block; margin-top: 5px;">
                            نام کاربری باید یکتا باشد
                        </small>
                    </div>
                    
                    <div class="form-group">
                        <label for="fullname">نام و نام خانوادگی *</label>
                        <input type="text" id="fullname" name="fullname" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="province">استان *</label>
                        <select id="province" name="province" required>
                            <option value="">-- انتخاب استان --</option>
                            <option value="تهران">تهران</option>
                            <option value="اصفهان">اصفهان</option>
                            <option value="خراسان رضوی">خراسان رضوی</option>
                            <option value="فارس">فارس</option>
                            <option value="آذربایجان شرقی">آذربایجان شرقی</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="city">شهرستان / شهر *</label>
                        <input type="text" id="city" name="city" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="school">مدرسه *</label>
                        <input type="text" id="school" name="school" required>
                    </div>
                    
                    <button type="submit">ثبت نام</button>
                </form>
                
                <div class="links">
                    <p style="color: #666; margin-bottom: 15px;">قبلاً ثبت نام کرده‌اید؟</p>
                    <a href="javascript:void(0);" onclick="showTab('login')" class="link-btn">
                        🔐 ورود به سیستم
                    </a>
                </div>
            </div>
        </div>
        
        <script>
            // توابع مدیریت تب‌ها
            function showTab(tabName) {
                // غیرفعال کردن همه تب‌ها
                document.querySelectorAll('.tab-content').forEach(tab => {
                    tab.classList.remove('active');
                });
                document.querySelectorAll('.tab-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                
                // فعال کردن تب انتخاب شده
                document.getElementById(tabName + '-tab').classList.add('active');
                event.target.classList.add('active');
                clearMessage();
            }
            
            function showMessage(text, type = 'success') {
                const messageDiv = document.getElementById('message');
                messageDiv.textContent = text;
                messageDiv.className = `alert ${type}`;
                messageDiv.style.display = 'block';
                
                // پنهان کردن پیام پس از 5 ثانیه
                setTimeout(clearMessage, 5000);
            }
            
            function clearMessage() {
                document.getElementById('message').style.display = 'none';
            }
            
            // فرم لاگین
            document.getElementById('loginForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const username = document.getElementById('login-username').value.trim();
                
                if (!username) {
                    showMessage('لطفاً نام کاربری را وارد کنید', 'error');
                    return;
                }
                
                // ارسال درخواست به سرور برای بررسی کاربر
                fetch('/users/api/check_login/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({username: username})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        if (data.user_exists) {
                            showMessage(`خوش آمدید ${username}!`, 'success');
                            // در اینجا می‌توانید کاربر را به صفحه اصلی هدایت کنید
                            // window.location.href = '/users/dashboard/';
                        } else {
                            showMessage('کاربر یافت نشد. لطفاً ثبت نام کنید.', 'error');
                            showTab('register');
                            // پر کردن فیلد نام کاربری در تب ثبت نام
                            document.getElementById('username').value = username;
                        }
                    } else {
                        showMessage(data.message, 'error');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    showMessage('خطا در ارتباط با سرور', 'error');
                });
            });
            
            // فرم ثبت‌نام
            document.getElementById('registerForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const formData = {
                    username: document.getElementById('username').value.trim(),
                    fullname: document.getElementById('fullname').value.trim(),
                    province: document.getElementById('province').value,
                    city: document.getElementById('city').value.trim(),
                    school: document.getElementById('school').value.trim()
                };
                
                // اعتبارسنجی اولیه
                if (!formData.username || !formData.fullname) {
                    showMessage('پر کردن فیلدهای ستاره‌دار الزامی است', 'error');
                    return;
                }
                
                fetch('/users/api/register/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify(formData)
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        showMessage(`ثبت نام ${formData.username} با موفقیت انجام شد!`, 'success');
                        this.reset();
                        // پس از 2 ثانیه به تب لاگین برگرد
                        setTimeout(() => {
                            showTab('login');
                            document.getElementById('login-username').value = formData.username;
                        }, 2000);
                    } else {
                        showMessage(data.message, 'error');
                        // اگر خطای تکراری بودن بود، به کاربر اطلاع بده
                        if (data.error_type === 'duplicate_username') {
                            showTab('login');
                            document.getElementById('login-username').value = formData.username;
                        }
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    showMessage('خطا در ارتباط با سرور', 'error');
                });
            });
            
            // تابع برای دریافت توکن CSRF
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            
            // نمایش تب لاگین به طور پیش‌فرض
            showTab('login');
        </script>
    </body>
    </html>
    """)

# صفحه ثبت نام (اگر می‌خواهید صفحه جداگانه داشته باشد)
def register_page(request):
    # این صفحه دیگر نیازی نیست چون در صفحه اصلی ادغام شد
    return redirect('/users/')

# API ثبت نام با بررسی تکراری بودن
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # اعتبارسنجی داده‌ها
            username = data.get('username', '').strip()
            fullname = data.get('fullname', '').strip()
            province = data.get('province', '').strip()
            city = data.get('city', '').strip()
            school = data.get('school', '').strip()
            
            if not all([username, fullname, province, city, school]):
                return JsonResponse({
                    'success': False,
                    'message': 'همه فیلدها باید پر شوند'
                }, status=400)
            
            # بررسی وجود کاربر با همین نام کاربری
            if UserProfile.objects.filter(username=username).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'این نام کاربری قبلاً ثبت شده است',
                    'error_type': 'duplicate_username'
                }, status=400)
            
            # بررسی وجود کاربر با همین نام کامل (اختیاری)
            if UserProfile.objects.filter(fullname=fullname).exists():
                return JsonResponse({
                    'success': False,
                    'message': f'کاربری با نام "{fullname}" قبلاً ثبت شده است',
                    'suggestion': 'اگر شما هستید، لطفاً با نام کاربری خود وارد شوید',
                    'error_type': 'duplicate_fullname'
                }, status=400)
            
            # ایجاد کاربر جدید
            user = UserProfile.objects.create(
                username=username,
                fullname=fullname,
                province=province,
                city=city,
                school=school
            )
            
            return JsonResponse({
                'success': True,
                'message': 'ثبت نام با موفقیت انجام شد',
                'user_id': user.id,
                'username': user.username,
                'created_at': user.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'داده‌های ارسالی معتبر نیست'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطای سرور: {str(e)}'
            }, status=500)
    
    return JsonResponse({'error': 'درخواست نامعتبر'}, status=405)

# API بررسی وجود کاربر
@csrf_exempt
def check_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            
            if not username:
                return JsonResponse({
                    'success': False,
                    'message': 'نام کاربری را وارد کنید'
                })
            
            # بررسی وجود کاربر در دیتابیس
            user_exists = UserProfile.objects.filter(username=username).exists()
            
            if user_exists:
                # اگر کاربر وجود دارد، اطلاعاتش را برگردان
                user = UserProfile.objects.get(username=username)
                return JsonResponse({
                    'success': True,
                    'user_exists': True,
                    'message': 'کاربر موجود است',
                    'user_data': {
                        'username': user.username,
                        'fullname': user.fullname,
                        'province': user.province,
                        'city': user.city,
                        'school': user.school,
                        'created_at': user.created_at.strftime("%Y-%m-%d %H:%M:%S")
                    }
                })
            else:
                return JsonResponse({
                    'success': True,
                    'user_exists': False,
                    'message': 'کاربر یافت نشد'
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)
    
    return JsonResponse({'error': 'درخواست نامعتبر'}, status=405)

# صفحه داشبورد کاربر (اختیاری)
def dashboard(request):
    return HttpResponse("""
    <html dir="rtl">
    <head><title>داشبورد کاربر</title></head>
    <body style="text-align: center; padding: 50px;">
        <h1>داشبورد کاربر</h1>
        <p>این صفحه بعداً تکمیل خواهد شد</p>
        <a href="/users/">بازگشت</a>
    </body>
    </html>
    """)