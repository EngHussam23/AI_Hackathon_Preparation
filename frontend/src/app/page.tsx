import { FileUpload } from "@/components/FileUpload";
import { DocumentList } from "@/components/DocumentList";

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold">AI Document OCR</h1>
          <p className="text-muted-foreground mt-2">
            Smart Governance Document Processing System
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <div className="grid lg:grid-cols-2 gap-8">
          {/* Upload Section */}
          <div>
            <h2 className="text-2xl font-semibold mb-4">Upload Documents</h2>
            <FileUpload />

            {/* Info Cards */}
            <div className="mt-6 grid gap-4">
              <div className="p-4 border rounded-lg bg-card">
                <h3 className="font-semibold mb-2">Supported Documents</h3>
                <ul className="text-sm text-muted-foreground space-y-1">
                  <li>• Invoices & Receipts</li>
                  <li>• Resumes & CVs</li>
                  <li>• Reports & Contracts</li>
                  <li>• Images (PNG, JPG, JPEG)</li>
                  <li>• PDF Documents</li>
                </ul>
              </div>

              <div className="p-4 border rounded-lg bg-card">
                <h3 className="font-semibold mb-2">Features</h3>
                <ul className="text-sm text-muted-foreground space-y-1">
                  <li>• Advanced OCR Text Extraction</li>
                  <li>• Automatic Document Classification</li>
                  <li>• Structured Data Extraction</li>
                  <li>• Multi-language Support</li>
                  <li>• JSON Format Output</li>
                </ul>
              </div>
            </div>
          </div>

          {/* Documents List Section */}
          <div>
            <h2 className="text-2xl font-semibold mb-4">Your Documents</h2>
            <div className="border rounded-lg p-4 bg-card min-h-[400px]">
              <DocumentList />
            </div>
          </div>
        </div>

        {/* Stats Section */}
        <div className="mt-12 grid md:grid-cols-3 gap-6">
          <div className="text-center p-6 border rounded-lg bg-card">
            <p className="text-3xl font-bold text-primary">30-40%</p>
            <p className="text-sm text-muted-foreground mt-2">
              Time Reduction in Processing
            </p>
          </div>
          <div className="text-center p-6 border rounded-lg bg-card">
            <p className="text-3xl font-bold text-primary">10-15%</p>
            <p className="text-sm text-muted-foreground mt-2">
              Error Rate Improvement
            </p>
          </div>
          <div className="text-center p-6 border rounded-lg bg-card">
            <p className="text-3xl font-bold text-primary">5 Types</p>
            <p className="text-sm text-muted-foreground mt-2">
              Document Classification
            </p>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t mt-12">
        <div className="container mx-auto px-4 py-6 text-center text-sm text-muted-foreground">
          <p>AI-Powered Document Management for Smart Governance</p>
          <p className="mt-2">Built with Next.js, TailwindCSS, and Shadcn UI</p>
        </div>
      </footer>
    </div>
  );
}
