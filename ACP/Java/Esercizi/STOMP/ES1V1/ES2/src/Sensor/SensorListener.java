package Sensor;

import javax.jms.MessageListener;
import javax.jms.*;

class SensorListener implements MessageListener{
    
    private TopicSession tSess;
    private CodaCircolareMon coda;

    public SensorListener(TopicSession tSess, CodaCircolareMon coda){

        this.tSess = tSess;
        this.coda = coda;
    }
    
    @Override
    public void onMessage(Message message){
        
        TextMessage m = (TextMessage) message;
        TManager t = new TManager(tSess, coda, m);

        t.start();

    }


    
}
