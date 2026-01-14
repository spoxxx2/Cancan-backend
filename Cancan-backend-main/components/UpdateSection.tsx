export default function UpdateSection() {
  return (
    <section className="bg-gray-50 py-12 px-6 md:px-12">
      <h2 className="text-3xl font-bold text-gray-900 mb-6">📣 Founder’s Message — January 5, 2026</h2>
      <blockquote className="border-l-4 border-blue-500 pl-4 italic text-gray-700 mb-6">
        “At Cancan, we believe in building secure, transparent, and scalable systems that empower developers to move fast without compromising trust. Today’s update reflects our commitment to continuous improvement — from refining our Supabase integration to strengthening admin access controls. Thank you for being part of this journey.”
        <footer className="mt-4 text-right font-semibold">— Casey Canfield, CEO & Founder of Cancan</footer>
      </blockquote>

      <h3 className="text-2xl font-semibold text-gray-800 mb-4">🧬 Latest Simulated Research DOIs</h3>
      <ul className="list-disc list-inside text-gray-700 space-y-3">
        <li>
          <strong>DOI: 10.1234/cancan.2026.001</strong><br />
          <em>"Decentralized Identity Verification Using Supabase and Next.js"</em>
        </li>
        <li>
          <strong>DOI: 10.1234/cancan.2026.002</strong><br />
          <em>"Edge-First Architectures for Real-Time Admin Gatekeeping"</em>
        </li>
        <li>
          <strong>DOI: 10.1234/cancan.2026.003</strong><br />
          <em>"Simulated Data Streams for AI-Driven Access Control Testing"</em>
        </li>
      </ul>
    </section>
  );
}
