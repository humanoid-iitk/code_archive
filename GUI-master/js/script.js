// Connecting to ROS
    // -----------------

  var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
  });

  ros.on('connection', function() {
    console.log('Connected to websocket server.');
  });

  ros.on('error', function(error) {
    console.log('Error connecting to websocket server: ', error);
  });

  ros.on('close', function() {
    console.log('Connection to websocket server closed.');
  });

// Subscribing to a Topic
  // ----------------------

  var message8;
  var message9;
  var message10;
  var message11;
  var message12;
  var message13;
  var message14;
  var message15;
  var message16;
  var message17;



  var listener8 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor8_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });

  listener8.subscribe(function(message8){
    document.getElementById("1.1").textContent=message8.name;
    document.getElementById("2.1").textContent=message8.motor_ids;
    document.getElementById("3.1").textContent=message8.motor_temps;
    document.getElementById("4.1").textContent=message8.goal_pos;
    document.getElementById("5.1").textContent=message8.current_pos + ",";
    document.getElementById("6.1").textContent=message8.error;
    document.getElementById("7.1").textContent=message8.velocity;
    document.getElementById("8.1").textContent=message8.load;
    document.getElementById("9.1").textContent=message8.is_moving;
  });

  var listener9 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor9_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });

  listener9.subscribe(function(message9){
        document.getElementById("1.2").textContent=message9.name;
        document.getElementById("2.2").textContent=message9.motor_ids;
        document.getElementById("3.2").textContent=message9.motor_temps;
        document.getElementById("4.2").textContent=message9.goal_pos;
        document.getElementById("5.2").textContent=message9.current_pos + ',';
        document.getElementById("6.2").textContent=message9.error;
        document.getElementById("7.2").textContent=message9.velocity;
        document.getElementById("8.2").textContent=message9.load;
        document.getElementById("9.2").textContent=message9.is_moving;
  });

  var listener10 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor10_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener10.subscribe(function(message10){ 

        document.getElementById("1.3").textContent=message10.name;
        document.getElementById("2.3").textContent=message10.motor_ids;
        document.getElementById("3.3").textContent=message10.motor_temps;
        document.getElementById("4.3").textContent=message10.goal_pos;
        document.getElementById("5.3").textContent=message10.current_pos + ',';
        document.getElementById("6.3").textContent=message10.error;
        document.getElementById("7.3").textContent=message10.velocity;
        document.getElementById("8.3").textContent=message10.load;
        document.getElementById("9.3").textContent=message10.is_moving;
});

  var listener11 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor11_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener11.subscribe(function(message11){    
        document.getElementById("1.4").textContent=message11.name;
        document.getElementById("2.4").textContent=message11.motor_ids;
        document.getElementById("3.4").textContent=message11.motor_temps;
        document.getElementById("4.4").textContent=message11.goal_pos;
        document.getElementById("5.4").textContent=message11.current_pos + ',';
        document.getElementById("6.4").textContent=message11.error;
        document.getElementById("7.4").textContent=message11.velocity;
        document.getElementById("8.4").textContent=message11.load;
        document.getElementById("9.4").textContent=message11.is_moving;
});

  var listener12 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor12_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener12.subscribe(function(message12){    

        document.getElementById("1.5").textContent=message12.name;
        document.getElementById("2.5").textContent=message12.motor_ids;
        document.getElementById("3.5").textContent=message12.motor_temps;
        document.getElementById("4.5").textContent=message12.goal_pos;
        document.getElementById("5.5").textContent=message12.current_pos + ',';
        document.getElementById("6.5").textContent=message12.error;
        document.getElementById("7.5").textContent=message12.velocity;
        document.getElementById("8.5").textContent=message12.load;
        document.getElementById("9.5").textContent=message12.is_moving;
});

  var listener13 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor13_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener13.subscribe(function(message13){    


        document.getElementById("1.6").textContent=message13.name;
        document.getElementById("2.6").textContent=message13.motor_ids;
        document.getElementById("3.6").textContent=message13.motor_temps;
        document.getElementById("4.6").textContent=message13.goal_pos;
        document.getElementById("5.6").textContent=message13.current_pos + ',';
        document.getElementById("6.6").textContent=message13.error;
        document.getElementById("7.6").textContent=message13.velocity;
        document.getElementById("8.6").textContent=message13.load;
        document.getElementById("9.6").textContent=message13.is_moving;
});

  var listener14 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor14_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener14.subscribe(function(message14){          
   document.getElementById("1.7").textContent=message14.name;
        document.getElementById("2.7").textContent=message14.motor_ids;
        document.getElementById("3.7").textContent=message14.motor_temps;
        document.getElementById("4.7").textContent=message14.goal_pos;
        document.getElementById("5.7").textContent=message14.current_pos + ',';
        document.getElementById("6.7").textContent=message14.error;
        document.getElementById("7.7").textContent=message14.velocity;
        document.getElementById("8.7").textContent=message14.load;
        document.getElementById("9.7").textContent=message14.is_moving;});

  var listener15 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor15_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener15.subscribe(function(message15){

        document.getElementById("1.8").textContent=message15.name;
        document.getElementById("2.8").textContent=message15.motor_ids;
        document.getElementById("3.8").textContent=message15.motor_temps;
        document.getElementById("4.8").textContent=message15.goal_pos;
        document.getElementById("5.8").textContent=message15.current_pos + ',';
        document.getElementById("6.8").textContent=message15.error;
        document.getElementById("7.8").textContent=message15.velocity;
        document.getElementById("8.8").textContent=message15.load;
        document.getElementById("9.8").textContent=message15.is_moving;
  });

  var listener16 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor16_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener16.subscribe(function(message16){

        document.getElementById("1.9").textContent=message16.name;
        document.getElementById("2.9").textContent=message16.motor_ids;
        document.getElementById("3.9").textContent=message16.motor_temps;
        document.getElementById("4.9").textContent=message16.goal_pos;
        document.getElementById("5.9").textContent=message16.current_pos + ',';
        document.getElementById("6.9").textContent=message16.error;
        document.getElementById("7.9").textContent=message16.velocity;
        document.getElementById("8.9").textContent=message16.load;
        document.getElementById("9.9").textContent=message16.is_moving;  });

  var listener17 = new ROSLIB.Topic({
    ros : ros,
    name : '/motor17_controller/state',
    messageType : 'dynamixel_msgs/JointState'
  });
  listener17.subscribe(function(message17){

        document.getElementById("1.10").textContent=message17.name;
        document.getElementById("2.10").textContent=message17.motor_ids;
        document.getElementById("3.10").textContent=message17.motor_temps;
        document.getElementById("4.10").textContent=message17.goal_pos;
        document.getElementById("5.10").textContent=message17.current_pos;
        document.getElementById("6.10").textContent=message17.error;
        document.getElementById("7.10").textContent=message17.velocity;
        document.getElementById("8.10").textContent=message17.load;
        document.getElementById("9.10").textContent=message17.is_moving;  });
