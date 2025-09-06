import streamlit as st # 스트림릿에서 쓰는 별칭
import pandas as pd # 데이터 사용할 때 많이 쓰는거
from datetime import date
#1. 텍스트 작성하기
st.title("헤헤😊")
st.write("하이염")

#2. 웹에 게시된 csv파일 불러오기
url = "https://github.com/teacher188-netizen/blank-app/blob/main/meals_data.csv"+"?raw=true"
df = pd.read_csv( url, encoding = 'cp949') #한국어 데이터기 때문에 오류가 없도록
#df. 데이터 불러오기(dataframe) 표데이터를 정리하지 않아도 된다!
st.dataframe(df)

#3. 데이터 대시보드 만들기
st.write("오늘의 메뉴를 표 형태로 확인할 수 있어요.")
#오늘 날짜 불러오기
dt = str(date.today())
st.write(dt)
today_row = df.loc[df['급식일자']=='2025-09-08'] #df.loc 조건에 맞는 행 표시
st.write(today_row) #오늘 날짜에 해당하는 행 출력


#metric 활용하기
st.write("metric으로 통계 정보를 전광판 형태로 시각화할 수 있어요.")
st.title(today_row['요리명'].item())
st.metric("메뉴", today_row['요리명'].item() ,border=True)

#metric 열 구성하기
a, b= st.columns(2)
#a, b에 metric 만들기
a.metric("칼로리", today_row['칼로리정보(Kcal)'].item(), 1600-today_row['칼로리정보(Kcal)'].item(), border=True)
b.metric("탄수화물", today_row['탄수화물(g)'].item())

#4. 차트로 데이터 시각화하기

#4-1. 지도 만들기
map_data = pd.DataFrame({
    'lat': [37.485475, 37.497539, 37.498014],
    'lon': [126.501083, 126.486135, 126.569858],
    'school': ['인천영종고', '인천공항고', '인천중산고'],
    'students': [923, 662, 1109]
})

st.map(map_data, size = 'students')


#4-2. 선 그래프 만들기
st.line_chart(df, x='급식일자',y=['칼로리정보(Kcal)', '탄수화물(g)'])

#4-3. 막대 그래프 만들기
st.bar_chart(df, x ='요일', y ="칼로리정보(Kcal)", color = '급식일자' , horizontal = True) #horizontal: 수직수평 설정



#다양한 입력 기능

st.date_input("날짜를 선택할 수 있는 입력폼")
st.selectbox("항목 중 하나를 선택할 수 있는 입력폼", ["월", "화", "수", "목", "금"])
st.text_input("주관식 입력폼", placeholder="placehoder에 들어가는 값이 힌트가 됩니다.")
st.slider("슬라이더를 조정해서 값을 선택하는 입력폼", 1, 5)
st.radio("객관식 버튼 입력폼", ["1", "2", "3", "4", "5"])


#입력 기능을 하나로 묶기
#with: 각종 요소를 함께 묶어서 입력한 내용을 제출버튼으로 한 번에 제출 가능
with st.form("급식 의견 받아요"): 
    d = st.date_input("날짜를 선택할 수 있는 입력폼")
    w = st.selectbox("항목 중 하나를 선택할 수 있는 입력폼", ["월", "화", "수", "목", "금"])
    c = st.text_input("주관식 입력폼", placeholder="placehoder에 들어가는 값이 힌트가 됩니다.")
    s = st.slider("슬라이더를 조정해서 값을 선택하는 입력폼", 1, 5)
    r = st.radio("객관식 버튼 입력폼", ["1", "2", "3", "4", "5"])
    submitted = st.form_submitted_button("제출")


#제출 내용 확인
if submitted:
    #제출내용을 웹에 바로 보여줍니다.
    st.write(f"""
            with st.form 안에 들어있는 변수를 중괄호 안에 넣으면 변수와 문자를 함께 출력할 수 있어요.\n
            날짜: {d}
            """)

