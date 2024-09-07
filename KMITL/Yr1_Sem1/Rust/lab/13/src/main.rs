use std::fmt;
use std::fmt::Formatter;
use std::io;
use std::io::*;
use std::*;

fn main() {
    let mut text = fs::read_to_string(r"D:\Main\Work\KMITL\Rust\lab\13\src\GPSA.csv")
    .expect("Should have been able to read the file");
    let mut gps_vec: Vec<GPS> = Vec::new();
    text = text.replace(" ", "");

    for x in text.lines(){
      let n = x.split(",");
      let mut str_vec = n.collect::<Vec<&str>>();
      gps_vec.push(GPS {
        lati: str_vec[0].parse::<f64>().unwrap(),
        long: str_vec[1].parse::<f64>().unwrap()
      });
    }
    let (meanLat, meanLong) = meanGPS(&gps_vec);
    let (minLat, minLong) = minGPS(&gps_vec);
    let (maxLat, maxLong) = maxGPS(&gps_vec);
    let (sdLat, sdLong) = sdGPS(&gps_vec);
    let (seLat, seLong) = seGPS(&gps_vec);

    println!("Mean Latitude: {:.5}", meanLat);
    println!("Mean Longitude: {:.5}", meanLong);
    println!("Min Latitude: {:.5}", minLat);
    println!("Max Latitude: {:.5}", maxLat);
    println!("Min Longitude: {:.5}", minLong);
    println!("Max Longitude: {:.5}", maxLong);
    println!("Standard Deviation Latitude: {:.5}", sdLat);
    println!("Standard Deviation Longitude: {:.5}", sdLong);
    println!("Standard Error Latitude: {:.5}", seLat);
    println!("Standard Error Longitude: {:.5}", seLong);
    printHis(&gps_vec);

}

#[derive(Debug, Clone)]
struct GPS {
  lati: f64,
  long: f64
}

fn his( lat_long: &Vec<GPS> ) -> (Vec<[f64; 2]>, Vec<[f64; 2]>) {
  let dec = 0.00001;
  let mut lati_bins: Vec<[f64; 2]> = Vec::new();
  let mut long_bins: Vec<[f64; 2]> = Vec::new();
  for x in lat_long {
    let mut exist = false;
    for y in 0..lati_bins.len() {
      if (x.lati - lati_bins[y][0]).abs() < dec {
        lati_bins[y][1] += 1.0;
        exist = true;
      }
    }
    if exist == false {
      lati_bins.push([x.lati, 1.0]);
    }
    exist = false;
    for y in 0..long_bins.len() {
      if (x.long - long_bins[y][0]).abs() < dec {
        long_bins[y][1] += 1.0;
        exist = true;
      }
    }
    if exist == false {
      long_bins.push([x.long, 1.0]);
    }
  }
  (lati_bins, long_bins)
}

fn printHis( lat_long: &Vec<GPS> ) {
  let (lati_bins, long_bins) = his(lat_long);
  println!("Latitude Histogram");
  for x in lati_bins {
    let star = "*".repeat(x[1] as usize);
    println!("{}: {}", x[0], star);
  }
  println!("Longitude Histogram");
  for x in long_bins {
    let star = "*".repeat(x[1] as usize);
    println!("{}: {}", x[0], star);
  }
}

fn meanGPS(gps : &Vec<GPS>) -> (f64, f64) {
  let mut meanLat = 0.0;
  let mut meanLong = 0.0;
  let mut count = 0.0;
  for x in gps{
    meanLat += x.lati;
    meanLong += x.long;
    count += 1.0;
  }
  return (meanLat / count, meanLong / count);
}

fn minGPS(gps : &Vec<GPS>) -> (f64, f64) {
  let mut minLat = gps[0].lati;
  let mut minLong = gps[0].long;
  for x in gps{
    if x.lati < minLat {
      minLat = x.lati;
    }
    if x.long < minLong {
      minLong = x.long;
    }
  }
  return (minLat, minLong);
}

fn maxGPS(gps : &Vec<GPS>) -> (f64, f64) {
  let mut maxLat = gps[0].lati;
  let mut maxLong = gps[0].long;
  for x in gps{
    if x.lati > maxLat {
      maxLat = x.lati;
    }
    if x.long > maxLong {
      maxLong = x.long;
    }
  }
  return (maxLat, maxLong);
}

fn sdGPS(gps : &Vec<GPS>) -> (f64, f64) {
  let meanLat = meanGPS(gps).0;
  let meanLong = meanGPS(gps).1;
  let mut sdLat = 0.0;
  let mut sdLong = 0.0;
  let mut count = 0.0;
  for x in gps{
    sdLat += (x.lati - meanLat).powf(2.0);
    sdLong += (x.long - meanLong).powf(2.0);
    count += 1.0;
  }
  return ((sdLat/count).sqrt(), (sdLong/count).sqrt());
}

fn seGPS(gps : &Vec<GPS>) -> (f64, f64) {
  let sdLat = sdGPS(gps).0;
  let sdLong = sdGPS(gps).1;
  //let count = gps.len() as f64;
  //return (sdLat/count.sqrt(), sdLong/count.sqrt());
  return (sdLat * 111139.0, sdLong * 107963.0);
}

