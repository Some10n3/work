import express from "express"
import mysql from "mysql"
import cors from "cors"
import nodemailer from "nodemailer"

const app = express()

app.use(express.json())

app.use(cors())

const db = mysql.createConnection({
  host: "localhost",
  port: "3306",
  user: "root",
  password: "Some10n3",
  database: "profile_database",
})

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'chanasorn.neo@gmail.com',
    pass: 'arerjqrqkneoehyj'
  }
})

const sendEmail = (data) => {

  const senderName = data.name
  const senderEmail = data.email
  const text = data.text

  const mailOptions = {
    from: senderEmail,
    to: 'chanasorn.neo@gmail.com',
    subject: 'From' + senderName + ' : ' + senderEmail,
    text: text,
  }

  console.log(mailOptions)

  transporter.sendMail(mailOptions, (err, info) => {
    if (err || senderName === '' || senderEmail === '' || text === '') {
      console.log(err)
    }
    else {
      console.log('Email sent: ' + info.response)
    }
  })
}


app.listen(8080, () => 
  console.log('Server running on port 8080')
)

app.get('/', (req, res) => {
  const receivedData = req.body;
  res.json({ message: 'Data received successfully' });
})

app.get('/courses', (req, res) => {
  db.query("SELECT * FROM profile_database.courses", (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.send(result)
      // console.log(result)
    }
  })
})

app.post('/email', (req, res) => {
  const receivedData = req.body;
  console.log(receivedData)
  res.json({ message: 'Data received successfully' });
  sendEmail(receivedData)
})