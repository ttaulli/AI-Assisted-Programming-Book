import * as React from "react";
import { createRoot } from "react-dom/client";
import { SparkApp, PageContainer, Input, Button, Card } from "@github/spark/components";
import { Envelope } from "@phosphor-icons/react";
import { useKV } from "@github/spark/hooks";

function NewsletterForm() {
  // State for managing email input
  const [email, setEmail] = React.useState("");
  // State for tracking submission status
  const [isSubmitted, setIsSubmitted] = React.useState(false);
  // Use KV store to persist emails
  const [subscribers, setSubscribers] = useKV("newsletter-subscribers", []);

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (email) {
      // Add new email to subscribers list
      const newSubscribers = [...subscribers, { 
        email, 
        timestamp: new Date().toISOString() 
      }];
      setSubscribers(newSubscribers);
      setIsSubmitted(true);
      setEmail("");
    }
  };

  return (
    <SparkApp>
      <PageContainer maxWidth="small">
        <Card>
          {/* Show success message if form was submitted */}
          {isSubmitted ? (
            <div className="text-center p-4">
              <h2 className="text-lg font-semibold mb-2">Thank you for subscribing!</h2>
              <p className="text-fg-secondary">You'll receive our updates soon.</p>
              {/* Allow signing up another email */}
              <Button 
                className="mt-4"
                onClick={() => setIsSubmitted(false)}
              >
                Subscribe another email
              </Button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="p-4">
              <h2 className="text-lg font-semibold mb-4">Subscribe to our Newsletter</h2>
              <div className="space-y-4">
                {/* Email input with envelope icon */}
                <Input
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  icon={<Envelope />}
                  id="email-input"
                />
                {/* Submit button */}
                <Button 
                  variant="primary" 
                  type="submit"
                  className="w-full"
                >
                  Subscribe
                </Button>
              </div>
            </form>
          )}
        </Card>
      </PageContainer>
    </SparkApp>
  );
}

// Render the application
const root = createRoot(document.getElementById("root"));
root.render(<NewsletterForm />);