import os

#fala meu caro leitor, oque está abaixo são as funções em python
#Barra de ferramentas é salvar e etc já a barra de navegação é os arquivos 


clear = lambda: os.system('clear') #clear serve pra limpar a tela

sleep = lambda: os.system('sleep 2') #sleep serve pra fazer a tela pausar por determinado tempo
exibirmenu = lambda: os.system('figlet BabyCode 21') # exibe banner
def menu_do_babycode21(): #essa função é pra exibir o menu principal do programa
     exibirmenu()
     print ('''\033[1;33mCriado por:\033[0m\033[1;37m Gabriel Kelzer\033[0m
\033[1;33mVersão:\033[0m\033[1;37m Primeira\033[0m
\033[1;33mLançamento:\033[0m\033[1;37m 2025\033[0m
                         \033[1;41mATENÇÃO:\033[0m

\033[1;36m    Este Script serve para exibir o Código-Fonte de algumas
  Views, as views são tudo o que possa interagir ou não com
  o usuário do aplicativo.\033[0m\033[1;31m#utilize todas as funções do Script!
\033[0m
\033[1;31m[\033[0m\033[1;37m 01\033[0m\033[1;31m ]\033[0m \033[1;33mTEXT VIEW     \033[0m              \033[1;31m [\033[0m\033[1;37m 02\033[0m\033[1;31m ] \033[0m\033[1;33mIMAGE VIEW\033[0m
\033[1;31m[\033[0m\033[1;37m 03\033[0m\033[1;31m ]\033[0m \033[1;33mEDIT TEXT     \033[0m              \033[1;31m [\033[0m \033[1;37m04 \033[0m\033[1;31m]\033[0m\033[1;33m BUTTON\033[0m
\033[1;31m[\033[0m\033[1;37m 05\033[0m\033[1;31m ]\033[0m \033[1;33mRADIO BUTTON  \033[0m              \033[1;31m [\033[0m\033[1;37m 06\033[0m\033[1;31m ]\033[0m\033[1;33m SAIR\033[0m
               \033[1;33m<\033[0m\033[1;36m----------===\033[0m\033[1;33m0\033[0m\033[1;36m===----------\033[1;33m>\033[0m
     ''') #Meu caro leitor, essa é a última função.


#Logo abaixo tem algumas váriaveis para ajudar o programa a funcionar
MENU_BABYCODE21 = "0"


while MENU_BABYCODE21 != "06":
      clear()
      menu_do_babycode21()
      MENU_BABYCODE21 = input('''\033[1;31mツ\033[0m \033[1;37m-\033[0m \033[1;32mESCOLHA UM NÚMERO: \033[0m''')
      clear()

      match MENU_BABYCODE21:
          case "01":
               print ('''
                         \033[1;41mESCOLHA 01:\033[0m
\033[1;37m
<TextView
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="Inserindo um texto na janela"
      />
\033[0m               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "02":
               print ('''
                        \033[1;41m ESCOLHA 02: \033[0m
\033[1;37m
<ImageView
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:src="@drawable/ic_launcher_foreground" />
\033[0m               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "03":
               print ('''
                        \033[1;41m ESCOLHA 03: \033[0m
\033[1;37m
<EditText
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:hint="Entre com seu nome"
      android:inputType="textPersonName"
      />
\033[0m               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "04":
               print ('''
                        \033[1;41m ESCOLHA 04: \033[0m
\033[1;37m
<Button
      android:id="@+id/btnEntrar"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="Entrar" />
\033[0m               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "05":
               print ('''
                        \033[1;41m ESCOLHA 05: \033[0m
\033[1;37m
<RadioGroup
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <RadioButton
       android:id="@+id/sexo masculino"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="Masculino" />

    <RadioButton
       android:id="@+id/sexo_feminino"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="Feminino" />
</RadioGroup>
\033[0m               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m+\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "06":
               print ('''
                        \033[1;41m ESCOLHA 06: \033[0m
\033[1;37m
    Obrigado por utilizar o meu programa, peço que você se
   inscreva no meu canal do YouTube\033[0m\033[1;33m @gabrielkelzer \033[0m\033[1;31m! \033[0m
               ''')
               OP_PAUSAR = input(' \033[1;31m[\033[0m \033[1;37m!\033[0m \033[1;31m]\033[0m \033[1;37m-\033[0m \033[1;32mAPERTE ENTER PARA SAIR:\033[0m')
          case _:    #Essa opção é somente se as anteriores não foram atendidas
               menu_do_tedkelzer()
               print ('\033[1;31m[ x ] - ESCOLHA INVÁLIDA ! \033[0m')
               sleep()


