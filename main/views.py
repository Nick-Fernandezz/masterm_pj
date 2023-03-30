from django.shortcuts import render

from .models import SocialClub, Moderators, Feedbacks, LegalInformation
from .models import FormBid as FormBidDB
from .forms import FormBid
from  .scripts.parseYT import findVideoFrame
# Create your views here.


def index(request):

    socialclubs = SocialClub.objects.all()
    moderators = Moderators.objects.all()
    feedbacks = Feedbacks.objects.filter(status=True)
    legalInformations = LegalInformation.objects.filter(visible=True)

    for feedback in feedbacks:
        feedback.video_url = findVideoFrame(feedback.video_url)

    sc_imgs = { 
        'WhatsApp': 'main/images/SociaClubs/whatsapp.svg',
        'VK': 'main/images/SociaClubs/vk-com.svg',
        'Telegram': 'main/images/SociaClubs/telegram.svg',
        'Facebook': 'main/images/SociaClubs/facebook.svg',
        'Instagram': 'main/images/SociaClubs/instagram.png',
        'OK': 'main/images/SociaClubs/odnoklassniki.svg',
        'TikTok': 'main/images/SociaClubs/tiktok.svg',
        'Twitter': 'main/images/SociaClubs/twitter.svg',
        'YouTube': 'main/images/SociaClubs/youtube.svg',
    }

    context = {
            'SCs': socialclubs, 
            'moderators': moderators,
            'SC_imgs': sc_imgs,
            'feedbacks': feedbacks,
            'legal_infs': legalInformations
    }

    if request.method == 'POST':
        
        user_form_info = {
            'name':  request.POST.get("name", 'Undefined'),
            'email': request.POST.get('email', 'Undefined'),
            'phone': request.POST.get('phone', 'Undefined')
        }

        if (
            0 < len(user_form_info['name']) < 100 and 
            0 < len(user_form_info['email']) < 100 and
            0 < len(user_form_info['phone']) < 100 and
            user_form_info['phone'].isdigit()

        ):
            userform = FormBidDB(name=user_form_info['name'],
                                 email=user_form_info['email'],
                                 phone=user_form_info['phone']
                                 )
            userform.save()

            context['alert_message'] = 'Заявка успешно оставлена. Ожидайте звонка менеджера.'
            return render(request, 'main/index.html', context=context)
        else:
            context['alert_message'] = 'Ошибка в введенных данных. Перепроверьте данные и повторнно отправте форму.'
            return render(request, 'main/index.html', context=context)
    else:

        return render(request, 'main/index.html', context=context)
