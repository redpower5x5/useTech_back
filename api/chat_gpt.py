import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": """separate code into different files with following rules:
1) dont implement any component API
2) write code without additions
3) write imports to each components
4) name main component as App
code:
export const Header: React.FC = () => {
  return (
    <Styled.Header>
      <Styled.HeaderWrap>
        <Styled.HeaderLeft>
          <img src="" />
          <Styled.Menu>
            <Styled.Item>
              <Styled.Text2>Тексты</Styled.Text2>
            </Styled.Item>
            <Styled.Item>
              <Styled.Text3>Митапы</Styled.Text3>
            </Styled.Item>
            <Styled.Item>
              <Styled.Text4>Figma</Styled.Text4>
            </Styled.Item>
            <Styled.Item>
              <Styled.Text5>Заметки</Styled.Text5>
            </Styled.Item>
            <Styled.Item>
              <Styled.Text6>Дайджест</Styled.Text6>
            </Styled.Item>
            <Styled.Item>
              <Styled.VuesaxLinearSearchNormal>
                <Styled.VuesaxLinearSearchNormal>
                  <img src="" />
                </Styled.VuesaxLinearSearchNormal>
              </Styled.VuesaxLinearSearchNormal>
              <Styled.Text8>Поиск</Styled.Text8>
            </Styled.Item>
          </Styled.Menu>
        </Styled.HeaderLeft>
        <Styled.HeaderRight>
          <Styled.Social>
            <Styled.Text9>youtube</Styled.Text9>
            <Styled.Text10>vk</Styled.Text10>
            <Styled.Text11>telegram</Styled.Text11>
            <Styled.Text12>dprofile</Styled.Text12>
          </Styled.Social>
          <Styled.Vuesax>
            <Styled.VuesaxLinearSun>
              <Styled.VuesaxLinearSun>
                <img src="" />
              </Styled.VuesaxLinearSun>
            </Styled.VuesaxLinearSun>
          </Styled.Vuesax>
        </Styled.HeaderRight>
      </Styled.HeaderWrap>
      <Styled.Devider />
    </Styled.Header>
  )
}"""}
  ]
)

print(completion.choices[0].message.content)