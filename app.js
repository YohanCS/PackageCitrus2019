const express = require('express')
const app = express()
const port = 3000

const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();
const bodyParser = require('body-parser');
const nodeWebCam = require('node-webcam');
const fs = require('fs');

// specifying parameters for the pictures to be taken
var options = {
    width: 1280,
    height: 720, 
    quality: 100,
    delay: 1,
    saveShots: true,
    output: "jpeg",
    device: false,
    callbackReturn: "location"
};

// create instance using the above options
var webcam = nodeWebCam.create(options);

// capture function that snaps <amount> images and saves them with the given name in a folder of the same name
var captureShot = (amount, i, name) => {
    var path = `./images/${name}`;

    // create folder if and only if it does not exist
    if(!fs.existsSync(path)) {
        fs.mkdirSync(path);
    } 

    // capture the image
    webcam.capture(`./images/${name}/${name}${i}.${options.output}`, (err, data) => {
        if(!err) {
            console.log('Image created')
        }
        console.log(err);
        i++;
        if(i <= amount) {
            captureShot(amount, i, name);
        }
    });  
};

app.use(bodyParser.json());
captureShot(1, 1, 'ga2ry');

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index.html'));
  //__dirname : It will resolve to your project folder.
});

app.post('/', function (req, res) {
    console.log('button clicked');
  });

app.use(express.static('./assets/css/images/'));
app.use(express.static('./'));

//add the router
app.use('/', router);
app.listen(process.env.port || 3000);

console.log('Running at Port 3000');
