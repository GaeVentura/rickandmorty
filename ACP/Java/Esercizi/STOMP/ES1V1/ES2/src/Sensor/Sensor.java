package Sensor;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

public class Sensor {
    
    public static void main(String[] args){

        int D = 5;

        Hashtable<String,String> prop = new Hashtable<String,String>();
        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url","tcp://127.0.0.1:61616");
        prop.put("topic.TopicES2", "TopicES2");

        try{

            Context jNDI = new InitialContext(prop);

            Topic topic = (Topic) jNDI.lookup("TopicES2");
            TopicConnectionFactory tConnFact = (TopicConnectionFactory) jNDI.lookup("TopicConnectionFactory");
            TopicConnection tConn = tConnFact.createTopicConnection();
		    tConn.setClientID("MakeItLastConn_1");


            TopicSession tSess = tConn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            CodaCircolare coda = new CodaCircolare(D);
            CodaCircolareMon codaMon = new CodaCircolareMon(coda);

            SensorListener sL = new SensorListener(tSess, codaMon);

            System.out.println("THREAD SONO QUI");
		    TopicSubscriber sub = tSess.createDurableSubscriber(topic, "MakeItLastConn_1");
            sub.setMessageListener(sL); 
            TExecutor TExec = new TExecutor(codaMon);
            tConn.start();
            TExec.start();




            
        } catch (JMSException exception){
            exception.printStackTrace();
        }catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } 




    }
}
