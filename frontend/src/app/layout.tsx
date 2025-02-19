import "../styles/globals.css";
import Navbar from "@/components/Navbar";

export const metadata = {
  title: "Workout AI App",
  description: "AI-powered exercise recommendations",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="flex h-screen">
          <Navbar /> {/* Left-side navbar */}
          <main className="flex-1 p-8 overflow-y-auto bg-gray-100">
            {children} {/* Dynamic page content */}
          </main>
        </div>
      </body>
    </html>
  );
}
