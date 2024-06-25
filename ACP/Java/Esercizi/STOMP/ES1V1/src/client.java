

import java.util.Hashtable;
import java.util.Random;


import javax.naming.*;



import javax.jms.*;


public class client {

    public static void main(String[] args) {

        Hashtable <String,String> prop = new Hashtable<String,String> ();

        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url","tcp://127.0.0.1:61616");

        prop.put("queue.Richieste", "Richieste");
        prop.put("queue.Risposte","Risposte");


        try{

            Context jCont = new InitialContext(prop);
            Queue qRichieste = (Queue) jCont.lookup("Richieste");
            Queue qRisposte = (Queue) jCont.lookup("Risposte");
            QueueConnectionFactory qConnectionFactory = (QueueConnectionFactory) jCont.lookup("QueueConnectionFactory");
            QueueConnection qConn = qConnectionFactory.createQueueConnection();

            qConn.start();
            QueueSession qSession = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            clientListener cL = new clientListener();
            QueueReceiver qReceiver = qSession.createReceiver(qRisposte);
            qReceiver.setMessageListener(cL);   


            QueueSender qSend = qSession.createSender(qRichieste);
            MapMessage message = qSession.createMapMessage();


            for (int i = 0; i < 10; i++){
                
                if(i<5){
                    message.setJMSReplyTo(qRisposte);

                    message.setString("operazione", "deposita");
                    message.setInt("valore", getRandInt());
                    qSend.send(message);

                    System.out.println("[CLIENT] INVIATO MESSAGGIO DI DEPOSITA CON VALORE "+ message.getInt("valore"));
                    

                } else{
                    message.setJMSReplyTo(qRisposte);
                    message.setString("operazione", "preleva");
                    qSend.send(message);
                    System.out.println("[CLIENT] INVIATO MESSAGGIO DI PRELEVA");


                }
            }




        } catch (JMSException e){
            e.printStackTrace();
        } catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }






    }

    public static int getRandInt(){

        Random r = new Random();
        return r.nextInt(100);
            
    }
}