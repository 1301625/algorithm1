import sys
script, encoding, error= sys.argv


def main(language_file,encoding,errors):
    line = language_file.readline() # 한줄 씩 읽기


    if line: #만약 줄이 있다면
        line_print(line,encoding,errors)  #라인프린터 함수 호출
        return main(language_file,encoding,errors) #재귀 반복




def line_print(line,encoding,errors):
    next_language = line.strip()     #줄 공백 제거
    raw_bytes = next_language.encode(encoding,errors=errors) #유니코드를 바이트 열로 변환할 때는 인코드 encode
    cooked_bytes = raw_bytes.decode(encoding,errors=errors) #바이트 열을 유니코드로 변환할 때는 디코드 decode

    print(raw_bytes, "<->" ,cooked_bytes)


languages = open('file.txt',encoding='utf-8')

main(languages,encoding,error)


#'strict' 는 인코딩 에러가 있는 경우 ValueError 예외를 발생시킵니다. 기본값 None 은 같은 효과를 냅니다.
#python ex23.py utf-8 strict