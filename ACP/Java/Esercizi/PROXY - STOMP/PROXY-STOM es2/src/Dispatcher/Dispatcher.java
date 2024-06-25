package src.Dispatcher;

import java.util.Hashtable;


import javax.naming.*;
import javax.jms.*;

public class Dispatcher extends DispatcherProxy{


    public Dispatcher(String host, int port){
        super(host,port);
    }

    public void run_dispatcher(){
        
        Hashtable<String, String> prop = new Hashtable<String,String>();

        prop.put("java.naming.factory.initial","org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url","tcp://127.0.0.1:61616");

        prop.put("queue.Richiesta","Richiesta");

        try{

            Context jCont = new InitialContext(prop);
            Queue q = (Queue) jCont.lookup("Richiesta");
            QueueConnectionFactory qConnFact = (QueueConnectionFactory) jCont.lookup("QueueConnectionFactory");
            QueueConnection qConn = qConnFact.createQueueConnection();
            qConn.start();
            QueueSession qSess = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueReceiver qReceiver = qSess.createReceiver(q);

            DispatcherListener dL = new DispatcherListener(qConn, this);
            qReceiver.setMessageListener(dL);

                



        }catch (JMSException e){
            e.printStackTrace();
        } catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }



    }
    
}
