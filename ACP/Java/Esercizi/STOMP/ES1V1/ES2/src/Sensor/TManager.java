package Sensor;

import javax.jms.*;

public class TManager extends Thread{

    
    @SuppressWarnings("unused")
    private TopicSession tSess;
    private CodaCircolareMon coda;
    private TextMessage message;

    public TManager(TopicSession tSess, CodaCircolareMon coda, TextMessage message){
        this.coda = coda;
        this.tSess = tSess;
        this.message = message;
    }

    public void run(){

       try {
        coda.put(message.getText().toString());
    } catch (JMSException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }
        



    }
    
}
