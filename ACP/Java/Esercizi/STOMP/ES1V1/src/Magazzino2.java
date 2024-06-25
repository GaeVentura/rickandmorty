
import java.util.Hashtable;
import java.util.Random;

import javax.jms.JMSException;
import javax.jms.MapMessage;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueReceiver;

import javax.jms.QueueSession;
import javax.jms.Session;
import javax.naming.InitialContext;
import javax.naming.*;

public class Magazzino2 {

    public static void main(String[] args) {

        CodaCircolare c = new CodaCircolare(5);

        CodaWrapperSem coda = new CodaWrapperSem(c);


        Hashtable <String,String> prop = new Hashtable<String,String> ();

        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url","tcp://127.0.0.1:61616");

        prop.put("queue.Richieste", "Richieste");
        prop.put("queue.Risposte","Risposte");


        try{

            Context jCont = new InitialContext(prop);


            QueueConnectionFactory qConnectionFactory = (QueueConnectionFactory) jCont.lookup("QueueConnectionFactory");
            Queue qRichieste = (Queue) jCont.lookup("Richieste");
            QueueConnection qConn = qConnectionFactory.createQueueConnection();
            qConn.start();
            QueueSession qSession = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);

            QueueReceiver qRec = qSession.createReceiver(qRichieste);

            System.out.println("[SERVER] AVVIATO");

            while(true){
                MapMessage mm = (MapMessage) qRec.receive();

                MagThread t = new MagThread(mm, coda, qConn);
                t.start();

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
