package Extractor;

import javax.jms.*;



public class ExtractorDataListener implements MessageListener{

    private TopicConnection tConn;
    private Topic tempTopic;
    private Topic pressTopic;

    public ExtractorDataListener(TopicConnection tConn, javax.jms.Topic tempTopic2, javax.jms.Topic pressTopic2){

        this.tConn = tConn;
        this.tempTopic = tempTopic2;
        this.pressTopic = pressTopic2;
        
    }

    @Override
    public void onMessage(javax.jms.Message message) {

        MapMessage mm = (MapMessage) message;
        try {
            String tipo = new String(mm.getString("type"));
            Integer value = mm.getInt("value");

            TopicSession tSess = tConn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            
            if(tipo.equalsIgnoreCase("temperature")){
                TopicPublisher pub = tSess.createPublisher(tempTopic);
                TextMessage pubMessage = tSess.createTextMessage();
                pubMessage.setText(value.toString());
                pub.publish(pubMessage);

            } else {
                TopicPublisher pub = tSess.createPublisher(pressTopic);
                TextMessage pubMessage = tSess.createTextMessage();
                pubMessage.setText(value.toString());
                pub.publish(pubMessage);
               
            }
        } catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }



    }
    
}
