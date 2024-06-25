package Client;

import java.util.Hashtable;
import java.util.Random;

import javax.naming.*;
import javax.jms.*;


public class Client {
    public static void main(String[] args) {
        
        Hashtable<String,String> prop = new Hashtable<String,String>();

        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.data","data");

        try{
            String tipo = new String(args[0]);
            Context jCont = new InitialContext(prop);

            Topic topic = (Topic) jCont.lookup("data");
            TopicConnectionFactory tConnFact = (TopicConnectionFactory) jCont.lookup("TopicConnectionFactory");
            TopicConnection tConn = tConnFact.createTopicConnection();
            tConn.start();

            TopicSession tSess = tConn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            TopicPublisher pub = tSess.createPublisher(topic);

            int NUM_RICHIESTE = 20;

            for(int i = 0; i < NUM_RICHIESTE; i++){
                MapMessage mm = tSess.createMapMessage();
                mm.setString("type", tipo);

                if(tipo.equalsIgnoreCase("temperature")){

                    int RandomTemperature = getRandTemp();

                    mm.setInt("value", RandomTemperature);

                } else {

                    int RandomPressure = getRandPress();
                    mm.setInt("value", RandomPressure);
                }

                pub.publish(mm);

            }
            

        } catch (JMSException e ){
            e.printStackTrace();
        } catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

    public static int getRandTemp(){

        Random r = new Random();

        return r.nextInt(100);
    }
    
    public static int getRandPress(){

        Random r = new Random();
        
        int x = r.nextInt(50) + 1000;
        return x;
    }
}
