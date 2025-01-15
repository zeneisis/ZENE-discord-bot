#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord 
import os 
import random 
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO
import pandas as pd

class communicate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        cmd = message.content.lower()
                
        if 'siuu' in cmd:
            await message.channel.send (file=discord.File(f'zene/data/video/siu.mp4'))

        if cmd == 'tôi bị xúc phạm':
            await message.channel.send('OMAE CỐ TÌNH CHỬI WATASHI DESU KA? TỪ TANJOUBI ĐẾN KONNICHI, WATASHI ĐÃ ĐƯỢC OSOWARU NÊN HITO, WATASHI KHÔNG BAO GIỜ XÚC PHẠM DARE CẢ, OMAE LÀM VẬY LÀ TONDEMONAI DAYO.TUY WATASHI CÓ HƠI WIBU SUKOSHI, DEMO WATASHI LUÔN ĐẶT NIỀM TIN VÀO ANIME VÀ SỐNG ĐÚNG KIỂU TRONG ANIME, ANIME LÀ 1 THỨ GÌ ĐÓ CAO CẢ HƠN CẢ GENJITSU, WATASHI ĐÃ LÀM THEO VÀ HỌC TẬP THEO TỪ ANIME, WATASHI ĐÃ ĂN UỐNG NGỦ NGHĨ THEO ĐÚNG GIỜ CỦA ANIME MÀ KHÔNG LÀM PHIỀN DARE, ĐÔI LÚC WATASHI CÓ CHỬI VÀO OMAE NO KAO NHƯ INU, DEMO SAU ĐÓ BLOCK NÓ THÌ WATASHI KHÔNG LÀM VIỆC ĐÓ NỮA, MAIKAI MAIKAI WATASHI MUỐN CHỬI DARE WATASHI ĐỀU COI ANIME VÀ GHI NHỚ RẰNG KHÔNG NÊN CHỬI NGƯỜI ĐÓ NỮA !! WATASHI ĐÃ CỐ GẮNG HIỀN HẬU ĐẾN MỨC MUỐN THÀNH HOTOKE RỒI MÀ KARERA VẪN KHÔNG ĐỂ WATASHI YÊN LÀ SAO, YABAI WATASHI KHÔNG NÊN GHI RA NHỮNG TỪ NÀY DEMO THẰNG YAROU SÚC VẬT NÓ LÔI WATASHI NO NA RA ĐỂ CHỬI, THỨ AHO SHUKU SEIBUTSUGAKU KAGAKU BUNGAKU, VẬY LÀ ĐỦ, ĐỪNG ĐỂ WATASHI TRIGGERED VÀ WATASHI DẠY OMAE CÁCH ĐỂ HỌC TẬP VÀ LÀM THEO TẤM GƯƠNG CỦA ANIME NỮA!, THẾ NHÉ INU WA KUSO O TABERU')

        if cmd == 'tôi bị đe dọa':
            await message.channel.send('Mấy thằng ranh con trong đây đừng có nghĩ tao hay đùa trên cái mạng ảo này mà nghĩ ngoài đời tao là một thằng wibu hèn hạ đéo dám ra đường hay trầm cảm, tự kĩ nhé. Thật ra bố mày đéo phải một thằng wibu bệnh hoạn như chúng mày nghĩ đâu lũ óc cặc ạ. Tao đây là otaku đàng hoàng chân chính nhá. Kể từ khi lọt lòng tới nay tao đã cày hơn 10 triệu bộ anime và từ việc xem anime mỗi ngày tao đã thông thạo được 50 thứ tiếng trên toàn thế giới cùng với khả năng đọc vị bất kỳ ai. Chưa hết đâu. Kể từ năm 2017, khi mà xem One Punch Man tao đã giác ngộ được mọi triết lý trên đời và quyết tâm bảo vệ nền hòa bình thế giới. Vì lẽ đó nên tao đã tập tành như Saitama, mỗi ngày 1000 cái hít đất, 1000 cái gập bụng, 1000 cái bật nhảy và chạy 100km (gấp mười lần idol của tao). Và chưa đầy nửa năm tao đã luyện thành mình đồng da sắt, chỉ cần thằng nào đụng đến tao thì một cái búng tay cũng đủ để nó bay ra ngoài vũ trụ với vận tốc gấp 10 lần tốc độ ánh sáng. Nếu thằng nào trong này cả gan chửi tao thì nên biết tao là ai trước đi, đề phòng chết khi nào không hay đấy.')

        if cmd == 'có đứa chửi wibu':
            await message.channel.send('ĐỊT CON ĐĨ MẸ NHÀ MÀY LÚC SÚC VẬT, WIBU THÌ ĐÃ SAO HẢ MẤY CON CHÓ ĂN CỨC RẢNH LỒN KHÔNG CÓ CHUYỆN GÌ LÀM ĐI GATO VS WIBU HẢ? WIBU ĂN HẾT CÁI LỒN CON ĐĨ MẸ MÀY HAY GÌ CỨ HỞ TÍ WIBU LÀ SAO HẢ CÁI CON THÚ HOANG RÁC RƯỞI, ĐỊT HẾT CÁC ĐỜI TỔ TÔNG GIA PHẢ NHÀ CON ĐĨ MẸ MÀY, TAO WIBU THÌ SAO? TỤI MÀY KO ĐC LÀM WIBU NHƯ TỤI TAO RỒI TỤI M TỨK HẢ? TỤI MÀY ĐÉO CÓ GỐI ÔM CỦA REM ĐỂ ĐỤ NÊN TỨK HẢ? TỤI MÀY ĐÉO CÓ THIỂU NĂNG NHƯ TỤI TAO TỤI MÀY TỨK HAY GÌ? TAO LÀ 1 WIBU CHÂN CHÍNH NÊN ĐỪNG ĐỤNG VÔ TỤI TAO, NẾU CÒN ĐỤNG VÔ THÌ TAO SẼ HOÁ ZORO CẦM 3 THANH KIẾM CHÉM MÀY RA HÀNG TRĂM MẢNH RỒI CHO CÁ SẤU ĂN ĐÓ, ĐỤ MẸ TỤI T NGỒI K CŨNG CÓ ĂN NÈ ĐÂU NHƯ TỤI M LÀM NHƯ CHÓ TỚI CUỐI THÁNG MỚI CÓ LƯƠNG ĐÂU, TỤI TAO NGỒI K ĂN BÁT VÀNG NÈ CON ĐĨ MẸ TỤI MÀY, TAO TỨK QUÁ MÀ, DÒNG ĐĨ NỨNG LỒN, NỨNG CẶC GÌ ĐÂU K À :rage::rage::rage::rage::rage::rage::rage:')

        if cmd == 'có đứa chửi waifu của tôi':
            await message.channel.send('CÂM CÁI MỒM CHÓ MÀY LẠI THẰNG LỒN SÚC VẬT NÀY. BỐ MÀY ĐÃ NÓI MÀY BAO NHIÊU LẦN RỒI RỒI LÀ ĐỊT CÁI LỒN MẸ MÀY ĐỪNG BAO GIỜ LẤY WAIFU NGƯỜI KHÁC RA LÀM TRÒ ĐÙA RỒI HẢ HÊ NHƯ KIỂU NHƯ MÌNH HÀI HƯỚC LẮM ẤY ĐỊT CON MẸ MÀY ĐÉO CÓ LIÊM SỈ THÌ THÔI TAO ĐÉO NÓI NHƯNG CON NGƯỜI CHỨ CÓ PHẢI CON CẶC ĐÂU MÀ ĐỂ TAO PHẢI NHẮC LẠI NHIỀU LẦN ĐẾN NHƯ VẬY. TAO ĐÉO PHẢI DẠNG THÍCH NỔI NÓNG CŨNG CHẢ PHẢI LOẠI VÔ HỌC NHƯNG TAO CÓ THỂ NÓI THẲNG MÀY ĐÉO KHÁC GÌ MỘT THẰNG RÁC RƯỞI, RIÊNG Ở ĐIỂM MÀY ĐEM VỢ NGƯỜI KHÁC RA LÀM TRÒ ĐÙA THÌ ĐÃ BIẾT ĐƯỢC MÀY KHÔNG THUA GÌ MỘT THẰNG CHÓ ĐẺ RỒI. MÀY CÓ THỂ CÂM CON MẸ NÓ MIỆNG VÀO VÀ CÚT RA KHỎI CUỘC ĐỜI TAO. VÀ ĐỪNG ĐỂ TAO PHẢI NHÌN THẤY CÁI BẢN MẶT CHÓ ĐẺ CỦA MÀY MỘT LẦN NỮA ĐỤ MÁ THẰNG SÚC VẬT THÍCH LÔI NGƯỜI KHÁC RA LÀM TRÒ ĐÙA. MÀY XÚC PHẠM REM THÌ CHÍNH LÀ MÀY ĐỤNG ĐẾN TAO. MỘT HAI LẦN THÌ TAO ĐÉO NÓI. ĐÂY ĐÃ LÀ QUÁ NHIỀU LẦN RỒI. TAO ĐÉO THỂ NÀO CHỊU ĐỰNG ĐƯỢC NỮA. CÚT CON MẸ MÀY RA KHỎI CUỘC ĐỜI TAO NGAY VÀ LUÔN THẰNG LỒN BÒ CÁI BÚ DÁI CON BÒ ĐỰC.')

        if cmd == 'có đứa chửi otaku':
            await message.channel.send('Ừ Otaku tụi tao thế đấy rồi sao :))) trẻ trâu dell có quyền làm người đấy rồi sao :))) nói ra mấy cái câu chỉ trích người khác rằng họ họ là súc vật thì tụi mày cũng vậy thôi :))) không hiểu anime vì tụi mày chưa coi những bộ ý nghĩa nên tụi mày không biết lí do tụi tao thích :)) nói thiệt tuy cũng thích tự nhận là Otaku thế đấy nhưng tao dell nhận thằng này làm đồng loại nhé :)) dell phải cứ một thằng tự nhận là Otaku não bò thì cứ vơ cả những người khác cũng vậy :))) đâu phải đứa nào nghiện Anime cũng trẻ trâu họ xem đơn giản không phải để lấy cái danh đâu Anime cũng truyền tải nhiều thứ rất ý nghĩa :))) chúng mày nếu vẫn cứ ghét Otaku bọn tao thì tùy dell thích nói chuyện với lũ rảnh lz ngồi chê bai người khác :))))')

        if cmd == 'bị xúc phạm nặng nề':
            await message.channel.send('Địt con mẹ mày mày thích mất dạy không thằng lồn? Đụ đỉ mẹ mày con súc vật nông dân móng chân vàng đừng có để tao phải tìm thấy cái mặt lồn nhà mày rồi tao lại bửa nát tử cung khai thông buồng trứng con mẹ mày đấy. Địt con mẹ mày mày thích mất dạy không thằng lồn đụ đỉ con mẹ mày đừng để tao phải tìm ra cái mặt lồn con mẹ mày rồi tao lại tọng vào lồn con đĩ mẹ mày 1000 cái xà beng nung đỏ và 100 tấn xi măng bít lồn con đĩ mẹ mày địt cả lò nhà mày địt từ hoa kỳ sang pháp địt từ pháp sang việt nam địt từ lồn mẹ mày sâu tới tâm trái đất địt cả họ hàng nhà mày mày thích mất dạy không đụ thằng cha con gái mẹ mày thằng lồn thất bại của tạo hóa đụ con đĩ bà già ông cố nội mày thằng cức người để tao gặp mày lần nữa thì đụ con đĩ mẹ mày 1001 cái sextoy đâm vào lồn con mẹ mày. Đụ con đĩ mẹ mày con súc vật lấc cấc mồm lồn còn hôi sữa mà cứ mở họng ra là tỏ vẻ bố thiên nhiên mẹ thiên hạ à con súc vật cái lồn chó má cả lò nhà mày chỉ là vật lót đường thứ lót dái cho tao mà thôi cho nên đừng có để bố mày phải tìm ra cái mặt lồn con đĩ mẹ mày rồi tao lại bít xi măng chằng mạng nhện bện lá khoai cái lồn mẹ mày lại nhé.')

        if cmd == 'cần dẹp từ simp':
            await message.channel.send('Cái từ "SIMP" nên được dẹp mẹ đi. Chỉ đơn giản là như này, đàn ông tôn trọng phụ nữ hoặc một ai đó tôn trọng người khác thì việc đó không cứ nên được cộp mác là "simp". Mấy thằng trẻ trâu ngày nay còn chả biết cách chùi đít nhưng nhiều lúc lại thích dùng mấy cái từ mà chả có nghĩa quái gì cả. Simp là dành cho một người đàn ông quá xem trọng một cô nàng nào đó và xem cô nàng tựa như vua chúa vậy. Từ khi nào mà việc thể hiện sự cảm thông, thân thiết và tôn trọng đối với một người phụ nữ lại được xem như là một hành vi simp vậy ? Cứ như thể việc thể hiện bất cứ thứ gì tôn trọng hoặc ngưỡng mộ đối với phái nữ thì đều được xem như là điều tồi tệ ấy. Thật sự là cái lòn què gì zậy ??? Tại sao việc ai đó quan tâm đến phái nữ lại làm phiền mấy người đến vậy cơ chứ ? Làm ơn hãy biết điều hơn và CÂM CÁI CON MẸ MỒM LẠI ĐI !!')

        if cmd == 'quá ghê gớm':
            await message.channel.send('Quá ghê gớm....🌚😳\nVà đây là Folontilô!😱😱\nFolontilô ui... 🥶🥶👿😳một tình huống múa phải nói là cực 👿gắt!!\n*music🤯\nThẹn thùng hùng nhìn em quay gót đi mãi😞😞💔\nAnh đứng chết lặng trong mưa😭😭\nDù rằng bên😊😊 em đã có ai\nNhưng nơi đây anh 🤗🤗🥱vẫn còn chờ...')

        if 'là...' in cmd:
            await message.channel.send('...là Folontilô!😱😱\nFolontilô ui... 🥶🥶👿😳một tình huống múa phải nói là cực 👿gắt!!\n*music🤯\nThẹn thùng hùng nhìn em quay gót đi mãi😞😞💔\nAnh đứng chết lặng trong mưa😭😭\nDù rằng bên😊😊 em đã có ai\nNhưng nơi đây anh 🤗🤗🥱vẫn còn chờ...')

        if cmd == 'bạn luôn đúng':
            await message.channel.send('Ok ok bạn là nhất, nhất bạn luôn Bạn luôn đúng, tôi mới là người sai Bạn thắng mình thua được chưa ? Bạn xứng đáng là kẻ nắm giữ đáp án chính xác của nhân loại Bạn mà đã nói là không thể sai được. Bạn nói chí phải, không ai làm lại bạn được luôn. Bạn nói đúng thế, mình cũng phải gật gù thay bạn đó. Bạn nói không trật vào đâu được, siêu thật đấy. Cứ cho là bạn đúng đi, bạn đúng, bạn đúng nhất. Ồ bạn nói đúng thật đó, sao giờ mình mới nhận ra nhỉ? Có ai từng nói với bạn rằng ý kiến của bạn rất hay không? Công nhận đấy, mình cũng nghĩ giống bạn. Mình biết bạn sẽ không làm mình thất vọng mà! Bạn khiến mình phải nể phục đó! Ồ ra là vậy, cảm ơn bạn nhiều nha! Vâng bạn nói mình xin nghe ạ. Lời của bạn làm mình rơi nước mắt luôn đó')

        if cmd == 'hảo hán':
            a = random.choice(os.listdir('zene/data/image/haohan'))
            await message.channel.send(file=discord.File(f'zene/data/image/haohan/{a}'))

        if cmd == 'nhóm sắp bị điều tra':
            await message.channel.send('Trong trường hợp nhóm này bị điều tra bởi các cơ quan trực thuộc bộ công an (hoặc các tổ chức chính trị tương tự phục vụ cho nhà nước CHXHCNVN), tôi khẳng định mình không liên quan tới nhóm hoặc những cá nhân khác trong nhóm này. Tôi không rõ tại sao mình lại có mặt ở đây vào thời điểm này, có lẽ tài khoản của tôi đã được thêm bởi một bên thứ ba. Tôi cũng xin khẳng định rằng mình không hề giúp sức cho những hành động chống phá Đảng và nhà nước của các thành viên trong nhóm này')

        if cmd == 'nhóm đã bị điều tra':
            await message.channel.send('Nhóm này đã bị điều tra bởi các cơ quan trực thuộc Bộ Công an (và/hoặc các tổ chức chính trị tương tự phục vụ cho nhà nước CHXHCNVN). Cơ quan điều tra (CQĐT) khẳng định các thành viên trong này liên quan tới nhóm hoặc những cá nhân khác trong đây. CQĐT biết rõ tại sao các thành viên lại có mặt ở đây vào thời điểm này, tài khoản của họ không được thêm bởi một bên thứ ba mà chính họ tự tham gia vào đây. Các nhân viên của CQĐT cũng xin khẳng định rằng những hành động chống phá Đảng và Nhà nước đã được thực hiện bởi các thành viên trong nhóm này. Nhà nước CHXHCNVN cũng không quên khẳng định quyết tâm chiến thắng đại dịch Covid-19, nhấn mạnh chủ quyền không thể tranh cãi với quần đảo Hoàng Sa và Trường Sa, cũng như tính chính nghĩa của cuộc chiến giải phóng người dân Campuchia khỏi thảm họa diệt chủng Kmer đỏ')

        if cmd == 'ảo ma':
            await message.channel.send('Dcm ảo ma Lazada Estonia Latvia Lithuania Austria Albania Croatia Serbia Slovenia Bulgaria Romania Russia Slovakia Canada Cuba Guatemala Jamaica Argentina Bolivia Colombia Venezuela Georgia Saudi Arabia Syria India Sri Lanka China Mongolia North Korea South Korea Cambodia Indonesia Malaysia Myanmar Australia Algeria Ghana Libya Nigeria Tunisia Maria Ozawa nhảy chachacha và Nobita làm Shizuka nhòe đi Mascara thật đấy')

        if cmd == 'cuộc đua giữa báo và chó săn':
            await message.channel.send('Năm 1908, người ta tổ chức cuộc đua giữa Báo Cheetah và những con chó săn, để xem Báo Cheetah có thực sự nhanh nhất thế giới như lời đồn hay không.\nĐiều bất ngờ đến khi cuộc đua diễn ra. Đàn chó cố hết sức lao đi còn con Báo thì thậm chí chẳng thèm nhúc nhích. Đám đông phẫn nộ, chỉ 1 người đàn ông đứng tuổi vẫn lặng im quan sát. Và rồi ông bất ngờ lên tiếng khiến tất cả phải im lặng:  **Khi bạn biết mình là số 1, bạn không cần phải chứng minh nó với bọn ngu** ')

        if cmd == 'xaolon':
            a = random.choice(os.listdir('zene/data/image/xaolon'))
            await message.channel.send(file=discord.File(f'zene/data/image/xaolon/{a}'))

        if cmd == '300 bài code thiếu nhi':
            a = [
                'Bà hàng xóm nhà mình đây, trước đi buôn đồng nát, tình cờ có thằng sinh viên khoa cntt nó bán đống sách cũ. Thế nào mà bà ấy mua "300 bài code thiếu nhi" cầm về đọc. Rồi sáng đi mua đồng nát, tối về đọc sách, cuối tuần ra quán net thực hành. Sáu tháng sau bà ấy khăn gói lên HN đi phỏng vấn, cũng nhờ code trên giấy nhiều mà mấy bài "white board" bà ấy làm ngon ơ. Cũng 5 năm rồi, giờ đang làm lead ở một công ty khá lớn.\nĐúng là cái nghề này mang lại cơ hội đổi đời cho nhiều người.',

                'Quê tôi miền biển, có gia đình cạnh nhà làm nghề chài lưới. Bữa đi kéo lưới, thấy gì nặng nặng tưởng được mẻ cá to, ai ngờ toàn sách là sách. Nào là "300 bài code thiếu nhi", "Lập trình căn bản", " Machine Learning", "Deep learning", "AI"...\nA định vất đi nhưng nhà mấy đời k biết mặt chữ là gì nên quyết tâm cầm về gối đầu giường. Đi học bổ túc văn hóa ban đêm phổ cập con chữ.\nẤy thế mà bẵng đi 6 tháng tôi từ thủ đô về thăm A khoe giờ ở nhà làm freelancer cho cty gì ở Mỹ ấy, to lắm, lương xấp xỉ 1 củ Biden/năm.',

                'Gần nhà mình có ông tầm gần 30. bảo làm cà phê, tiêu mệt quá. Thế là khăn gói xuống tp học 1 khóa lập trình pithon dip leaning gì đó, xong rồi làm 300 bài code thiếu nhi luyện tập. Bữa mới nói chuyện khoe đang làm lương cũng 1 2k gì đó!',

                'Bác họ tui 46 rồi, chạy ba gác hoài mệt quá đi học lớp code cấp tốc. Học hết 2 tháng với làm hết bài trong cuốn 300 bài code thiếu nhi, xong apply vào công ty kia làm mảng data science mỗi tháng lương net hơn 400tr.',

                'Ông xe ôm xóm mình sinh năm 82, hôm trước chạy xe lớ ngớ thế nào rớt xuống cống, rồi nhặt được cuốn lập trình "code thiếu nhi" gì gì đó, về đọc đâu hơn 1 tháng rồi ra HN làm cho công ty trí tuệ nhân tạo to lắm, mới làm 1 năm mua được nhà HN, mua được thêm con mazda 6 rồi.',

                'Trước tôi đẩy xe hủ tiếu ngoài đường vô tình bắt gặp nhà nọ mở thời sự về blocktrain, thế là cứ ngày đi bán tối về coi NTN với tranh thủ coi clocktrain 1 xíu.Về nhà tối nào tôi cũng làm 3 bài trong "300 bài code thiếu nhi", mà sau 3 tháng cũng apply được công ty về tiền ảo. Giờ tôi đánh sang cả mảng AI nữa, mới viết app di dộng auto deepfake có người trả 300k$ chưa bán.',

                'Năm ngoái đi fuho sml ngoài công trình vô tình nhặt dc cuốn sách 300 bài lập trình dành cho thiếu nhi về nhà luyện tập theo sau 3 tháng tự tin apply 1 cty chuyên về ai, ml ở quận 1 lương 3k chưa thưởng hay phụ cấp đây.', 

                '6 tháng trước làm nhà hàng vất vả quá, trong lúc thái thịt đọc lướt được cuốn java căn bản với 300 bài code thiếu nhi. Bây giờ dev full stack lương 2,2k',

                'Mẹ thằng chú tôi làm sales sim số đẹp cho viettel đợt rồi đói ăn quá nên vất cho cuốn lập trình code thiếu nhi gì đấy, 6 tháng sau vào làm dev cứng FPT rồi , nghe bảo lương 2k vì ngành này đang hot',

                'Ông già tôi làm công nhân than đuối quá, muốn kiếm việc gì nhẹ hơn. Tôi giới thiệu ng khoá học HTML CSS PHP trên ucademy với làm bài tập trong cuốn 300 bài code thiếu nhi.\nSau 6 tháng, giờ ỗng ở nhà làm freelancer rung đùi hàng tháng tài khoản cứ bắn vào mấy ngàn $. Đang tính bảo bà già khỏi đi làm nữa ở nhà mà xài tiền.',
            ]
            await message.channel.send(random.choice(a))

        data_file = pd.read_excel('zene/data/command_data/command_link.xlsx')
        data_frame_file = pd.DataFrame(data_file)
        try:
            request = data_frame_file.loc[data_frame_file['Command'] == cmd, 'File_Location'].iloc[0]
            await message.channel.send(file=discord.File(request))
        except:
            ''

    @commands.command()
    async def hotro(self,ctx):
        await ctx.send('@here CÁC BẠN NHÂN VIÊN ƠI, CÁC BẠN HỖ TRỢ MÌNH VỚI. CÁC BẠN ƠI CÁC BẠN ĐƯA NHẦM ĐỒ CHO MÌNH CÁC BẠN ƠI. CÁC BẠN NHÂN VIÊN HỖ TRỢ ƠI. CÁC BẠN HỖ TRỢ MÌNH KHÔNG CÁC BẠN ƠI. CÁC BẠN ĐIẾC À CÁC BẠN ƠI HỖ TRỢ MÌNH KHÔNG CÁC BẠN ƠI.')

    @commands.command()
    async def avt(self, ctx, *, memberavt: discord.Member=None):
        if memberavt == None:
            user_avt_url = ctx.author.avatar
        else:
            user_avt_url = memberavt.avatar
        await ctx.send(user_avt_url)
    
    @commands.command()
    async def haha(self, ctx, *, memberavt: discord.Member=None):
        if memberavt == None:
            memberavt = ctx.author

        haha = Image.open('zene/data/image/haha.jpg')
        asset = memberavt.avatar.replace(size = 256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        haha.paste(pfp, (470, 120))
        haha.save('zene/data/image/cache.jpg')
        await ctx.send(file=discord.File(r'zene/data/image/cache.jpg'))

    @commands.command()
    async def tv(self, ctx, *, memberavt: discord.Member=None):
        if memberavt == None:
            memberavt = ctx.author

        asset = memberavt.avatar.replace(size = 256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        tv = Image.open('zene/data/image/tv/FB_IMG_1573133316104.jpg')
        tv.paste(pfp.resize((100,100)),(95,115))
        tv.save('zene/data/image/cache.jpg')

        await ctx.send(file=discord.File(f'zene/data/image/cache.jpg'))

    @commands.command()
    async def bonk(self,ctx, *, god: discord.Member=None):
        try:
            if god.id == 262844868919951360:
                await ctx.send('Không được đánh Onii-sama :angry:')
            else:
                a = random.choice(os.listdir('zene/data/image/bonk'))
                await ctx.send(file=discord.File(f'zene/data/image/bonk/{a}'))
        except:
            a = random.choice(os.listdir('zene/data/image/bonk'))
            await ctx.send(file=discord.File(f'zene/data/image/bonk/{a}'))

    @commands.command()
    async def xinloi(self,ctx):
        await ctx.send('Tôi đã sai, sai từ ngay giây phút đầu tranh luận cùng bạn. Tôi đáng lẽ phải nhận ra điều này sớm hơn. Cảm ơn bạn vì đã dành thời gian chỉ ra những sai lầm trong luận điểm của tôi. Bạn hoàn toàn chính xác. Bạn là nhất.')

    @commands.command()
    async def sapnupuas(self,ctx):
        await ctx.send('Xin lỗi về sự bất lịch sự này những em biết đấy, khi nói lên những thứ rực rỡ tuyệt đẹp mà tạo hóa ban tặng chắc chắn không thể nào bỏ qua được thân hình của người phụ nữ. Vậy liệu em có thể cho anh chiêm ngưỡng một chút về nét đẹp sâu sắc, tuyệt vời ấy nằm ở bên trong lớp vải mỏng manh mà em khoác lên không?')

    @commands.command()
    async def anxin(self,ctx):
        a = [
            'Mong được giúp đỡ ạ.Mẹ em trước đây làm công nhân vệ sinh nhưng hồi đầu tháng 5 mẹ em thấy mệt và kiệt sức nên đi khám thì phát hiện bị ung thư tử cung, sau đó vì sức khỏe giảm sút nên xin nghỉ để về nhà may đồ nhấc nồi để bán ngoài chợ, từ ngày chợ cấm bán đến giờ mẹ em đang rất khó khăn vì phải lo thuốc than hàng ngày và cả tiền phòng trọ nữa. Vc Em thì làm bên nhà hàng nên cũng bị nghỉ dịch 2 tháng nay và cũng có 2 con nhỏ nữa nên cũng khó khăn ko có khả năng phụ giúp dc gì. Kính mong các nhà hảo tâm giúp đỡ cho mẹ em ít lương thực để vượt qua được lúc khó khăn này.E biết khi em đăng lên đây sẽ có những người nói là em bất hiếu vì không giúp được cho mẹ e trong những lúc như thế này nhưng thật quá khó khăn nên em xin được mọi người giúp đỡ. Địa chỉ KDC An Tây A - Gần chợ , gần KCN Việt Hương 2,Bình Duong. E xin chân thành cám ơn rất nhiều',

            'Mọi người ơi. Thật sự bí quá em mới  viết lên, giờ em k còn tiền. Đã nợ 3 tháng tiền nhà rồi,còn mấy ngày nữa qua tháng thứ 4 . Em làm bên cty xây dựng,cty nợ lương em 2 tháng + 3 thang dịch là 5 tháng em chưa nhận dc tiền,vì có con nhỏ 2t và vợ mang bầu 4thang nên k còn tiền.em k biết phải làm sao hết. Mong có ai giúp đỡ cho em mượn tạm mỗi người 10K - 20K góp lại đóng dc bao nhiêu thì đóng cho họ.Em sẽ lưu lại những người cho em vay sau này hết dịch em sẽ gởi lai.Neu ai cảm thấy ko vui vì stt này của em thì mong thông cảm bỏ qua cho em,em k biết làm sao mới đăng như vậy,xin đừng chửi rủa.Em đang mắc kẹt ở tâm dich Binh Dương. Em xin chân thành cảm ơn các mạnh thường quân và các nhà hảo tâm có lòng để cho bé nhà em có được hợp sữa uống với ạ',

            'Em xin các MTQ và các nhà HẢO TÂM, giúp cho vợ chồng em với ạ... em mới sinh bè trai dc  hơn 3 tháng, mà dịch em ko đi làm đc. 2 tháng nay em toàn phải ở nhà, ăn dè những đồng tiền ít còn dư 1 ít. Vì pải đóng tiền nhà trọ, rồi lại phải mua sữa cho bé. Vợ em vì thiếu thốn ko có chất, lên ko có sữa cho con bú. 1 tuần nay con em hết sữa em phải lấy nước cơm cho con uống, nhưng vì cháu càng ngày ngày gầy. Nên vợ chồng em ko còn cách nào khác, em mới phải lên đây xin mọi người giúp cho gia đình em với. Xin giúp cho con em xin ít sữa với ạ',

            'Em bị chồng bỏ. từ quê lên thuê nhà đi làm nuôi con. thất nghiệp 3 tháng nay. hết tiền trang trải. không tiền mua sữa cho con. lương thực cũng hết. giờ em phải làm sao ở nơi xứ lạ quê người này. không người thân họ hàng. con khóc suốt vì thiếu sữa. không biết cầm cự được bao lâu nữa. em bất lực. chỉ biết nhìn con mà khóc thôi. Xin mọi người Cứu giúp cho vài đồng lẻ. 10k. 20k. mua sữa cho con. Có chút lương thực để sống tạm qua mùa dịch này. Em vô cùng biết ơn mọi người. ❤️',

            'E bị tai biến, trong lúc hôn mê thì chồng e bỏ đi, giờ dịch bệnh một mình em phải vừa nuôi con nhỏ 1 tuổi, vừa nuôi mẹ già 70 tuổi bị mù,1 tuần nay con em hết sữa em phải lấy nước cơm cho con uống, nhưng vì cháu càng ngày ngày gầy. Nên vo chong e ko còn cách nào khác, em mới phải lên đây xin mọi người giúp cho gia đình em với. Xin giúp cho con em xin ít sữa với ạ. Em cảm ơn rất nhiều ạ.',

            'Mọi người giúp gia đình em với ạ ,ba của bé mất nên giờ tự một mình e đi sinh trong thời gian dịch bệnh không có người thân chăm sóc, bé mới sinh được 1 tháng mắc bệnh tim bẩm sinh phải trải qua 3 lần phẫu thuật tim chi phí hơn 600tr nhưng vẫn không thành công , lần này bác sĩ nói phải thay tim thì bé mới có thể tiếp tục sống sót ạ , tình hình bé rất nguy kịch nhưng hiện tại gia đình không còn đủ khả năng để lo cho bé , e xin các mạnh thường quân có thể giúp đỡ gia đình e cứu mạng bé gái ạ và hiện bé đang cấp cứu ở bệnh viện chợ rẫy ạ.',
            
            'Hiện tại hoàn cảnh gia đình rất khó khăn ạ ..do lúc trước dịch .nhà em có 1 số chuyện nên phải mướn 2 trọ ( cùng 1 nhà trọ) và vẫn đi làm bình thường ...nhà em 3 người .2 người  làm thì đúng lương tới tháng là có ..còn em do cty bị ảnh hưởng dịch từ năm rồi . .nên toàn ứng tiền .nhưng tầm 10_15 ngày thì em được ứng ,.thì khi ứng ra còn không đủ tiền ăn .với trọ .và lúc cty bắt đầu nghĩ do chỉ thị ..đã được 1 tháng thì cả nha em đều không chống nổi ..vì tiền trọ giảm được 250k 1 phòng ...và tiền ăn cũng không đủ ...và cảm thấy là sắp trụ không nổi ròi ạ ...cuộc đời em đi đâu thấy ai đi lang thang em cho này kia ,và thấy rất tội ngta ..nhưng không ngờ lại có một ngày em lại phải đăng lên xin trợ giúp như vậy,,buồn vô cùng ạ .Và em đã và đang đăng kí những phần quà nhưng không thấy được gì cả ...Hiện em rất muốn được về quê.nhưng nhà em ngay cả tiền ăn cũng không thì làm sao về được đây ạ ..em.ở cà mau.về là phải cách ly tập trung ..rất tốn tiền và em không còn khả năng xoay sở nữa ...phải nói là rất khó khăn .không còn tiền để ăn nữa ạ .Kính mong mọi người giúp đỡ cho em với ạ .Em rất cảm ơn mọi người',
        ]
        await ctx.send(random.choice(a))

    @commands.command()
    async def auzam(self,ctx):
        a = random.choice(os.listdir('zene/data/image/auzam'))
        await ctx.send(file=discord.File(f'zene/data/image/auzam/{a}'))

    @commands.command()
    async def nohorny(self,ctx):
        a = random.choice(os.listdir('zene/data/image/no_horny'))
        await ctx.send(file=discord.File(f'zene/data/image/no_horny/{a}'))

    @commands.command()
    async def wake(self,ctx):
        await ctx.send(file=discord.File(f'zene/data/video/wake.mp4'))

    @commands.command()
    async def cmd(self,ctx):
        cmd_list = pd.read_excel('zene/data/command_data/command_link.xlsx')
        data_frame_cmd_list = pd.DataFrame(cmd_list)
        await ctx.send(data_frame_cmd_list.loc[:,'Command'])

    @commands.command()
    async def samhoi(self,ctx):
        await ctx.send(f'Hãy từ bỏ tà dâm từ bỏ thủ dâm không xem các loại sách báo không xem các loại băng hình có nội dung kích dục. Sám hối nghiệp chướng đã tạo quyết từ nay không tái phạm. Thường xuyên niệm Phật để thân tâm được an lạc.\nNam Mô A Di Đà Phật.\nCon xin được sám hối tội nghiệp dâm dục và ý nghĩ, hành động nói những lời dâm uế để kích động ý dâm của người khác từ .\nCon xin được sám hối tất cả tội chướng của con đã tạo do : Thân, khẩu, ý gây ra từ vô lượng kiếp đến nay. Mong các vị oan gia trái chủ cho con 1 cơ hội tha thứ cho con cùng con nhất tâm niệm cùng đồng sanh về Tây Phương cực lạc.\nCon nguyện khi vãng sanh Tây Phương cực lạc sẽ dùng đạo lực cứu độ tất cả chúng sanh trong khắp pháp giới đều được sanh về thế giới cực lạc\nNữ sắc suy cho cùng cũng chỉ là da với thịt. Máu mủ tanh hôi. Cái bẫy luân hồi đau khổ vô lượng kiếp')

async def setup(bot):
    await bot.add_cog(communicate(bot))