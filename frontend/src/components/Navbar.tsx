import Link from "next/link"

export default function Navbar() {
    return (
        <nav className="h-full w-60 bg-gray-800 text-white p-6">
            <h2 className="text-3xl font-bold mb-6">Workout AI</h2>
            <ul className="space-y-4">
                <li>
                <Link href="/" className="hover:text-gray-300">Home</Link>
                </li>
                <li>
                <Link href="/profile" className="hover:text-gray-300">Profile</Link>
                </li>
                <li>
                <Link href="/recommendations" className="hover:text-gray-300">Recommendations</Link>
                </li>
            </ul>
        </nav>
    );
}