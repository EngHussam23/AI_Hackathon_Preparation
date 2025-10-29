# AI Document OCR - Frontend

A modern Next.js application for AI-powered document processing with OCR, classification, and data extraction.

## 🚀 Tech Stack

- **Next.js 16** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **TailwindCSS 4** - Utility-first CSS framework
- **Shadcn UI** - High-quality React components
- **Zustand** - Lightweight state management
- **TanStack Query** - Server state management
- **React Dropzone** - File upload functionality
- **Lucide React** - Beautiful icons
- **Axios** - HTTP client

## 📁 Project Structure

```
frontend/
├── src/
│   ├── app/              # Next.js App Router
│   │   ├── layout.tsx    # Root layout with providers
│   │   ├── page.tsx      # Homepage
│   │   └── globals.css   # Global styles
│   ├── components/       # React components
│   │   ├── ui/          # Shadcn UI components
│   │   ├── FileUpload.tsx
│   │   └── DocumentList.tsx
│   ├── stores/          # Zustand stores
│   │   └── ocrStore.ts  # OCR state management
│   ├── providers/       # Context providers
│   │   └── QueryProvider.tsx
│   ├── types/           # TypeScript definitions
│   │   └── ocr.ts       # OCR types
│   └── lib/             # Utility functions
│       ├── utils.ts     # Helper functions
│       └── api.ts       # API client
├── public/              # Static assets
├── .env.local.example   # Environment variables template
└── package.json         # Dependencies
```

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
cd frontend
npm install
```

This will install all required packages including:

- `zustand` - State management
- `@tanstack/react-query` - Server state
- `axios` - HTTP client
- `react-dropzone` - File uploads
- `clsx` & `tailwind-merge` - Utility functions
- `lucide-react` - Icons

### 2. Environment Variables

Create a `.env.local` file:

```bash
cp .env.local.example .env.local
```

Edit `.env.local` and set your backend API URL:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🎯 Features

### Current Features

- ✅ Drag & drop file upload
- ✅ Multi-file support (PDF, PNG, JPG, JPEG, GIF, BMP)
- ✅ Document list management
- ✅ Processing status tracking
- ✅ Zustand state management
- ✅ TanStack Query integration
- ✅ Responsive design
- ✅ Dark mode support

### Upcoming Features

- 🔜 Real-time OCR processing
- 🔜 Document classification
- 🔜 Structured data extraction
- 🔜 Results visualization
- 🔜 Export to JSON
- 🔜 Search and filter documents
- 🔜 Backend API integration

## 📝 State Management

### Zustand Store (OCR)

The app uses Zustand for client-side state management:

```typescript
const { documents, addDocument, removeDocument } = useOCRStore();
```

**Store Features:**

- Document upload tracking
- Processing status management
- OCR results storage
- LocalStorage persistence
- DevTools integration

### TanStack Query

For server state and API calls:

```typescript
const { data, isLoading } = useQuery({
  queryKey: ["ocrResult", documentId],
  queryFn: () => fetchOCRResult(documentId),
});
```

## 🎨 Adding Shadcn Components

To add new Shadcn UI components:

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
```

## 🔧 Available Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run start    # Start production server
npm run lint     # Run ESLint
```

## 📦 Key Dependencies

| Package               | Version | Purpose          |
| --------------------- | ------- | ---------------- |
| next                  | 16.0.0  | React framework  |
| react                 | 19.2.0  | UI library       |
| typescript            | ^5      | Type safety      |
| tailwindcss           | ^4      | Styling          |
| zustand               | latest  | State management |
| @tanstack/react-query | latest  | Server state     |
| axios                 | latest  | HTTP client      |
| react-dropzone        | latest  | File uploads     |

## 🌐 API Integration

The app is configured to connect to a Python backend API. Update the API URL in `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🚀 Deployment

### Build for Production

```bash
npm run build
npm run start
```

### Deploy to Vercel

```bash
vercel deploy
```

### Deploy to Other Platforms

The app can be deployed to:

- Vercel (recommended)
- Netlify
- AWS Amplify
- Docker container

## 🤝 Contributing

This is part of the AI Hackathon Preparation project. See the main README for contribution guidelines.

## 📄 License

MIT License - see LICENSE file for details.

---

**Built for Smart Governance AI Hackathon** 🏆
