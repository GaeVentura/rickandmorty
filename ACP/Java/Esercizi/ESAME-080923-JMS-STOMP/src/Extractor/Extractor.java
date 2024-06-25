package Extractor;

import java.util.Hashtable;

import javax.jms.JMSException;

import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;

import javax.jms.*;
import javax.naming.*;
import javax.naming.NamingException;



public class Extractor {

    public static void main(String[] args) {
        
        Hashtable<String,String> prop = new Hashtable<String,String>();

        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.data","data");
        prop.put("topic.temp","temp");
        prop.put("topic.press","press");


        try{
            Context jCont = new InitialContext(prop);

            Topic topicData = (Topic) jCont.lookup("data");
            Topic pressTopic = (Topic) jCont.lookup("press");
            Topic tempTopic = (Topic) jCont.lookup("temp");
            TopicConnectionFactory tConnFact = (TopicConnectionFactory) jCont.lookup("TopicConnectionFactory");
            TopicConnection tConn = tConnFact.createTopicConnection();
            tConn.setClientID("durableSubID");
            tConn.start();

            TopicSession tSess = tConn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            ExtractorDataListener eDL = new ExtractorDataListener(tConn, tempTopic, pressTopic);
            TopicSubscriber sub = tSess.createDurableSubscriber(topicData, "durableSubID");
            sub.setMessageListener(eDL);
            


            

            

        } catch (JMSException e ){
            e.printStackTrace();
        } catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    

    
    
    }

    
}
