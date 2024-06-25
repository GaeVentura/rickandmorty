


package ControlStation;
import javax.jms.*;
import java.util.Hashtable;
import java.util.Random;

import javax.naming.*;

public class ControlStation{

    public static void main(String[] args) {
        
        Hashtable<String,String> prop = new Hashtable<String,String>();
        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url","tcp://127.0.0.1:61616");
        prop.put("topic.TopicES2", "TopicES2");

        try{

            Context jNDI = new InitialContext(prop);

            Topic topic = (Topic) jNDI.lookup("TopicES2");
            TopicConnectionFactory tConnFact = (TopicConnectionFactory) jNDI.lookup("TopicConnectionFactory");
            TopicConnection tConn = tConnFact.createTopicConnection();
            tConn.start();

            TopicSession tSess = tConn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher pub = tSess.createPublisher(topic);

            TextMessage message = (TextMessage) tSess.createTextMessage();
            for(int i=0; i<20; i++){

                Thread.sleep(1000);

                int randInt = getRandInt();

                if (randInt == 0){
                    message.setText("startSensor"); 
                } else if (randInt == 1){
                    message.setText("stopSensor");
                } else {
                    message.setText("read");
                }
                
                pub.send(message);
            
            }

            pub.close();
            tSess.close();
            tConn.close();
            
        } catch (JMSException exception){
            exception.printStackTrace();
        } catch (InterruptedException e) {

            e.printStackTrace();
        } catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

    public static int getRandInt(){

        Random r = new Random();
        return r.nextInt(2);
            
    }

}