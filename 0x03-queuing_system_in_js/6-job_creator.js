import { createQueue } from 'kue';
var kue = require('kue')
   ,queue = kue.createQueue();

// Create an object containing the job data
const jobData = {
  phoneNumber: '0777698976',
  message: 'Hello there from your notification!',
};

// Create a queue named push_notification_code and create a job with the provided data
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Notification job failed');
      return;
    }
    console.log('Notification job created:', job.id);
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
