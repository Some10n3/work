use std::fmt;
use std::fmt::Formatter;
use std::io;
use std::io::*;

fn main(){
  /*
  let filE = fs::File::open("text.txt").expect("Unable to open file");
  let lines = io::BufReader::new(filE).lines();
  for line in lines {
    let line = line.unwrap();
    let nc = unpack_text_line(line, &mut freq_table);
  }
  */
  let mut vals = Vec::new();
  let mut count = 0;
  let mut structt = String::new();
  let mut agesum = 0;
  let mut person = 0;
  
  loop {
      //eprintln!("check loop");
      let mut text = read_text_line();
      
      if text.len() < 3 { break; }
      else {
          let n = text.split(": ");
          let str_vec = n.collect::<Vec<&str>>();

          if str_vec[0].to_string() == "job".to_string(){
              if count != 0{
                  printt(structt, vals[1..vals.len()].to_vec());
                  vals.clear();
              }
              structt = str_vec[1].to_string();
              person += 1;
          }

          if str_vec[0].to_string() == "age".to_string(){
              agesum += str_vec[1].parse::<u32>().unwrap();
          }

          vals.push(str_vec[1].to_string());
          //eprintln!("Vals => {:?}", vals[1..vals.len()].to_vec());
      }
      count += 1;
  }
  printt(structt, vals[1..vals.len()].to_vec());
  println!("Average age: {}", agesum/person);
}


#[derive(Debug, Copy, Clone)]
struct GPS {
  lati: f64,
  long: f64
}

fn show_position(gps : GPS) {
  const Degree: &str = "\u{00b0}";
  let position = gps;
  let mut lati_direction = "N";
  let mut long_direction = "E";
  if position.lati < 0.0 {
      lati_direction = "S";
  }
  if position.long < 0.0 {
      long_direction = "W";
  }
  print!{"{}{} {}, {}{} {}", position.lati, Degree, lati_direction, position.long, Degree, long_direction}
}

#[derive(Debug, Clone)]
struct teacher{
  name : String,
  age : u32,
  location : GPS,
  students : Vec::<String>,
}

#[derive(Debug, Clone)]
struct admiral{
  name : String,
  age : u32,
  location : GPS,
  ships : Vec::<String>,
}

#[derive(Debug, Clone)]
struct doctor{
  name : String,
  age : u32,
  location : GPS,
  patients : Vec::<String>,
}

trait employees {
  fn getName(&self);
  fn getAge(&self);
  fn getLocation(&self);
  fn getResponsibility(&self);
}

impl employees for teacher{
  fn getName(&self){
    println!("Teacher : {}", self.name);
  }
  fn getAge(&self){
    println!("Age : {}", self.age);
  }
  fn getLocation(&self){
    println!("Location : {}, {}", self.location.lati, self.location.long);
  }
  fn getResponsibility(&self){
      println!("Current Students : {:?}", self.students)
  }
}

impl employees for admiral{
  fn getName(&self){
    println!("Admiral : {}", self.name);
  }
  fn getAge(&self){
    println!("Age : {}", self.age);
  }
  fn getLocation(&self){
    println!("Location : {}, {}", self.location.lati, self.location.long);
  }
  fn getResponsibility(&self){
      println!("Current Ships : {:?}", self.ships)
  }
}

impl employees for doctor{
  fn getName(&self){
    println!("Doctor : {}", self.name);
  }
  fn getAge(&self){
    println!("Age : {}", self.age);
  }
  fn getLocation(&self){
    println!("Location : {}, {}", self.location.lati, self.location.long);
  }
  fn getResponsibility(&self){
    println!("Current Patients : {:?}", self.patients)
  }
}

impl fmt::Display for teacher {
  fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
      write!(f, "admiral({})\nAge : {}\nLatitude : {}\nLongitude : {}\nStudents : {:?})", self.name, self.age, self.location.lati, self.location.long, self.students)
  }
}

impl fmt::Display for admiral {
  fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
    write!(f, "Admiral({})\nAge : {}\nLatitude : {}\nLongitude : {}\nShips : {:?})", self.name, self.age, self.location.lati, self.location.long, self.ships)
  }
}

impl fmt::Display for doctor {
  fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
    write!(f, "Doctah({})\nAge : {}\nLatitude : {}\nLongitude : {}\nPatients : {:?})", self.name, self.age, self.location.lati, self.location.long, self.patients)
  }
}

fn read_text_line() -> String {
  let mut buffer = String::new();
  let _result = io::stdin().read_line(&mut buffer);
  buffer = buffer.trim().to_string();
  // eprintln!("Buffer read ({}) [{}]", buffer.len(), buffer );
  buffer
}

fn inp(structt: String, val: Vec<String>) -> (teacher, admiral, doctor){
  let g = GPS{
    lati: 0.0,
    long: 0.0,
  };
  let mut t1 = teacher{
      name: String::from(""),
      age: 0,
      location: g,
      students: Vec::new(),
  };

  let mut a1 = admiral{
      name: String::from(""),
      age: 0,
      location: g,
      ships: Vec::new(),
  };

  let mut d1 = doctor{
      name: String::from(""),
      age: 0,
      location: g,
      patients: Vec::new(),
  };
  
  if structt == "Teacher".to_string(){
      let lat_arr = val[2].split(", ").collect::<Vec<&str>>();
      t1 = teacher{
        name: val[0].clone(),
        age: val[1].parse::<u32>().unwrap(),
        location: GPS{
          lati: lat_arr[0].parse::<f64>().unwrap(),
          long: lat_arr[1].parse::<f64>().unwrap(),
        },
        students: val[3].split(",").map(|s| s.to_string()).collect(),
      };
  }
  else if structt == "Admiral".to_string(){
      let lat_arr = val[2].split(", ").collect::<Vec<&str>>();
      a1 = admiral{
        name: val[0].clone(),
        age: val[1].parse::<u32>().unwrap(),
        location: GPS{
          lati: lat_arr[0].parse::<f64>().unwrap(),
          long: lat_arr[1].parse::<f64>().unwrap(),
        },
        ships: val[3].split(",").map(|s| s.to_string()).collect(),
      };
  }
  else if structt == "Doctor".to_string(){
      let lat_arr = val[2].split(", ").collect::<Vec<&str>>();
      d1 = doctor{
        name: val[0].clone(),
        age: val[1].parse::<u32>().unwrap(),
        location: GPS{
          lati: lat_arr[0].parse::<f64>().unwrap(),
          long: lat_arr[1].parse::<f64>().unwrap(),
        },
        patients: val[3].split(",").map(|s| s.to_string()).collect(),
      };
  }
  return (t1, a1, d1);

}


fn printt(structt: String, val: Vec<String>){
  let (t1, a1, d1) = inp(structt, val.clone());
  print!("\n\n");
  if t1.name != "".to_string(){
      t1.getName();
      t1.getAge();
      t1.getLocation();
      t1.getResponsibility();
  }
  else if a1.name != "".to_string(){
      a1.getName();
      a1.getAge();
      a1.getLocation();
      a1.getResponsibility();
  }
  else if d1.name != "".to_string(){
      d1.getName();
      d1.getAge();
      d1.getLocation();
      d1.getResponsibility();
  }
  print!("\n\n");
}
