import { createQueue, Job } from 'kue';
const queue = createQueue();

// Define blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Define the sendNotification function
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track job progress
  job.progress(50);

  // Log notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Track job progress
  job.progress(100);

  // Notify job completion
  done();
}

// Process jobs from push_notification_code_2 queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running...');
