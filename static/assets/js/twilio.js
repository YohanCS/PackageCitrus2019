// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure
const accountSid = 'ACd2148cd345fe38a25fc343a796f81df7';
const authToken = '912d45179c831a138d6277f6ac9f5a51';
const client = require('twilio')(accountSid, authToken);

client.messages
  .create({
     body: 'This is the ship that made the Kessel Run in fourteen parsecs?',
     from: '+16572438103',
     to: '+16262712003'
   })
  .then(message => console.log(message.sid));


