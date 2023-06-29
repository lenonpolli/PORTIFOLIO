import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(actions: [],backgroundColor:Colors.green,) ,

      

      body: ListView(children: [

        
       Container(
         decoration: BoxDecoration(
          color: Colors.white,
         ),
                    // colors: [const Color.fromARGB(255, 15, 15, 15), Color(0xFF6D0264)])),
                    
        child: Column(
         
          children: [
            SizedBox(height: 20,),
            Container(
      
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  
            
                 Text(style: TextStyle(fontSize: 40,color: Colors.green),'Disponivel em qualquer lugar')
              ],
              
              ),
           
            ),
          
            SizedBox(height: 100,),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                 Image.asset('assets/images/teste.png',width: 500,height: 500,),
                  Image.asset('assets/images/tv.png',width: 500,),
              
              ],),
              SizedBox(height: 50,),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [

              Text(style: TextStyle(color: Colors.green,fontSize: 30),'Que tal um pouco de entretenimento ? Então você está no lugar certo!\n\nCom apenas um clique você pode conferir tudo sobre os nossos serviços!\n\n                             Clique no botão abaixo para saber mais !')

            ],),SizedBox(height: 30,),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [ ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                    onSurface: Colors.green,
                    elevation: 20,
                    shadowColor: Color(0xFFFF5E00),
                    
                  ),
                  child:
                   Text(style: TextStyle(fontSize: 40,fontWeight: FontWeight.bold),'TESTE GRATIS !'),
                  onPressed: () {},
                ),],),SizedBox(height: 100,),


            Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            
            children: [

             
                Card(
                  shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
                  
                  
                 color: Colors.green,
                  elevation: 20,
                  shadowColor:Color(0xFFFF5E00), 
                  child: Container(
                    
                    
                    child: Column(children: [
              
                    
                    
                    Text(style: TextStyle(fontSize: 40,color: Colors.white,fontWeight: FontWeight.bold),'PLANO BÁSICO'),
                    SizedBox(height: 20,),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Conexão Simultânea:1'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais em: SD/HD'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Disponíveis: + 400'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Adultos: Sim'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Filmes e Séries On Demand'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'+ 20.000 Conteúdos'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Teste Gratuito'),
                     Text(style: TextStyle(fontSize: 25,color: Colors.white),'Liberação Imediata após a confirmação do pagamento'),
                     Divider(height: 30,),
                     ElevatedButton( style: ElevatedButton.styleFrom(
                      primary: Colors.green,
                      onSurface: Colors.green,
                      elevation: 20,
                      shadowColor: Colors.black,
                      
                    ),
                    child:
                     Text(style: TextStyle(fontSize: 40,fontWeight: FontWeight.bold),'ASSINAR AGORA !'),
                    onPressed: () {},),Divider(height: 30,)
                  ],),
                ),
              ),
              Card(
                shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
                color: Colors.green,
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
                child: Container(
                  
                  
                  child: Column(children: [

                  
                  
                  Text(style: TextStyle(fontSize: 40,color:Colors.white,fontWeight: FontWeight.bold),'PLANO INTERMEDIARIO'),
                  SizedBox(height: 20,),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Conexão Simultânea:1'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais em: SD/HD/FHD'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Disponíveis: + 900'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Adultos: Sim'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Filmes e Séries On Demand'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'+ 20.000 Conteúdos'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Teste Gratuito'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Liberação Imediata após a confirmação do pagamento'),
                   Divider(height: 30,),
                   ElevatedButton( style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                    onSurface: Colors.green,
                    elevation: 20,
                    shadowColor: Colors.black,
                    
                  ),
                  child:
                   Text(style: TextStyle(fontSize: 40,fontWeight: FontWeight.bold),'ASSINAR AGORA !'),
                  onPressed: () {},),Divider(height: 30,)
                  
                ],)),),
                Card(
                  shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
                  color: Colors.green,
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
                borderOnForeground: true,
                child: Container(
                  
                  
                  child: Column(children: [

                  
                  
                  Text(style: TextStyle(fontSize: 40,color: Colors.white,fontWeight: FontWeight.bold),'PLANO AVANÇADO'),
                  SizedBox(height: 20,),
                  Text(style: TextStyle(fontSize: 25,color: Colors.white),'Conexão Simultânea:1'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais em: SD/HD/FHD/4K'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Disponíveis: + 1.200'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Adultos: Sim'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Filmes e Séries On Demand'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'+ 20.000 Conteúdos'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Teste Gratuito'),
                   Text(style: TextStyle(fontSize: 25,color: Colors.white),'Liberação Imediata após a confirmação do pagamento'),
                   Divider(height: 30,),
                   ElevatedButton( style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                    onSurface: Colors.green,
                    elevation: 20,
                    shadowColor: Colors.black,
                    
                    
                  ),
                  child:
                   Text(style: TextStyle(fontSize: 40,fontWeight: FontWeight.bold),'ASSINAR AGORA !'),
                  onPressed: () {},),Divider(height: 30,)
                ],)),)



          ],),SizedBox(height: 200,),

          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Card(
                shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
                child: 
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [

                     ElevatedButton( style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                    onSurface: Colors.green,
                    elevation: 20,
                    shadowColor: Colors.black,
                    
                  ),
                  
                  child:
                   Text(style: TextStyle(fontSize: 80,fontWeight: FontWeight.bold),'TESTE GRATUITO DE 4 HORAS!'),
                   
                  onPressed: () {})]



                    
                    

                  
                 
                  ),
                  
                  )]
                  ),SizedBox(height: 200,),
            Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly,children: [Card(
              color: Colors.green,
              shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
              
              child: Column(children: [
              

              
              
             
              Text(style: TextStyle(fontSize: 40,color: Colors.white),'Sem Fidelidade'),
              SizedBox(height: 20,),
              Text(style: TextStyle(fontSize: 25,color: Colors.white),'Cancele a hora que quiser sem taxas abusivas.')



            ]
            
            ),
            
            ),Card(
              shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
              color:Colors.green,
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
              child: Column(children: [
              
              Text(style: TextStyle(fontSize: 40,color: Colors.white),'Acesso Imediato'),
              SizedBox(height: 20,),
              Text(style: TextStyle(fontSize: 25,color: Colors.white),'Nosso suporte irá lhe atender de forma imediata')

            ]),),Card(
              shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
              color: Colors.green,
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
              child: Column(children: [
              Text(style: TextStyle(fontSize: 40,color: Colors.white),'Reembolso'),
              SizedBox(height: 20,),
              Text(style: TextStyle(fontSize: 25,color: Colors.white),'Em caso de insatisfação , devolvemos o seu dinheiro.')

            ]),)
            ]
            
            
            
            ,),SizedBox(height: 200,),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
              Text(style: TextStyle(fontSize: 40,color:  Colors.green,),'POR QUE COMPRAR O NOSSO SERVIÇO ?')
            ],),SizedBox(height: 200,),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [Card(
                shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
              color:Colors.green,
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
              child: Column(children: [

                

                
                  
                    Text(style: TextStyle(fontSize: 40,color: Colors.white,fontWeight: FontWeight.bold),'DISPONIBILIZAMOS'),
              SizedBox(height: 20,),
                
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Todos os canais abertos e fechados.'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais de assinatura(Combat,Premier).'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais 24hs(Cortesia).'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Canais Internacionais(Cortesia).'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Filmes e séries On Demand.'),
               




            ]),),Card(
              shape: RoundedRectangleBorder(side: BorderSide(color: Colors.black),borderRadius:BorderRadius.circular(20.0) ),
              color: Colors.green,
                elevation: 20,
                shadowColor:Color(0xFFFF5E00), 
              child: Column(children: [

              Text(style: TextStyle(fontSize: 40,color: Colors.white,fontWeight: FontWeight.bold),'DIFERENCIAIS'),
              SizedBox(height: 20,),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Suporte Seg a Seg das 08:00 as 22:00 hrs.'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Atualização de conteúdos semanalmente.'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Filmes e séries liberados!.'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Pós venda eficiente.'),
                Text(style: TextStyle(fontSize: 25,color: Colors.white),'Servidor próprio e nacional.'),
                

            ]),)],),SizedBox(height: 200,),

          Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children:
                 [
                  Text(style: TextStyle(fontSize: 40,color:  Colors.green,),'CONTATO'),
                   Text(style: TextStyle(color:  Colors.green,),'Telefone: (xx) - 49494-494949'),
                   Text(style: TextStyle(color:  Colors.green,),'Email: empresa@empresa.com.br')
                 
                  ],),
              
            ],
          )

         


      
          
       ] ),
        
        
      )
      
      
     ]));
     
  }
}

                  

           