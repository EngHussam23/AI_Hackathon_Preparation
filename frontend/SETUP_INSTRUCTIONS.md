# Frontend Setup Instructions

## 📦 Install Dependencies

Run this command in the `frontend` directory:

```bash
npm install zustand @tanstack/react-query @tanstack/react-query-devtools axios react-dropzone clsx tailwind-merge lucide-react
```

## ✅ What's Already Set Up

Your frontend now has:

1. **State Management**

   - ✅ Zustand store (`src/stores/ocrStore.ts`)
   - ✅ Document upload tracking
   - ✅ Processing status management
   - ✅ LocalStorage persistence

2. **Server State**

   - ✅ TanStack Query provider (`src/providers/QueryProvider.tsx`)
   - ✅ API client with Axios (`src/lib/api.ts`)
   - ✅ DevTools for debugging

3. **TypeScript Types**

   - ✅ OCR types (`src/types/ocr.ts`)
   - ✅ Document, OCRResult, ProcessingStatus enums
   - ✅ Structured data interfaces

4. **Components**

   - ✅ FileUpload with drag & drop
   - ✅ DocumentList with status tracking
   - ✅ Utility functions (cn helper)

5. **UI/UX**
   - ✅ Updated homepage with OCR interface
   - ✅ Layout with QueryProvider
   - ✅ Responsive design
   - ✅ Dark mode support

## 🚀 Run the Development Server

```bash
npm run dev
```

Then open http://localhost:3000 in your browser.

## 🔧 Environment Variables

Create a `.env.local` file (copy from `.env.local.example`):

```bash
cp .env.local.example .env.local
```

Set your backend API URL:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 📝 Project Structure Created

```
frontend/src/
├── app/
│   ├── layout.tsx          ✅ Updated with QueryProvider
│   ├── page.tsx            ✅ New OCR landing page
│   └── globals.css
├── components/
│   ├── FileUpload.tsx      ✅ Drag & drop component
│   └── DocumentList.tsx    ✅ Document management
├── stores/
│   └── ocrStore.ts         ✅ Zustand state management
├── providers/
│   └── QueryProvider.tsx   ✅ TanStack Query setup
├── types/
│   └── ocr.ts              ✅ TypeScript definitions
└── lib/
    ├── utils.ts            ✅ Helper functions (cn)
    └── api.ts              ✅ Axios client
```

## 🎯 Next Steps

1. **Install dependencies** (command above)
2. **Run the dev server** (`npm run dev`)
3. **Test file upload** - Drag and drop files to see them in the list
4. **Connect backend** - Update `.env.local` when your Python API is ready
5. **Add Shadcn components** as needed:
   ```bash
   npx shadcn@latest add button
   npx shadcn@latest add card
   npx shadcn@latest add dialog
   ```

## 🐛 Troubleshooting

### Import Errors

If you see "Cannot find module" errors, make sure you ran:

```bash
npm install
```

### Port Already in Use

If port 3000 is busy, Next.js will prompt you to use another port, or you can specify:

```bash
npm run dev -- -p 3001
```

### TypeScript Errors

Run type checking:

```bash
npx tsc --noEmit
```

## 📚 Documentation

- See `FRONTEND_README.md` for detailed documentation
- Check `src/types/ocr.ts` for type definitions
- Look at `src/stores/ocrStore.ts` for state management usage

---

**Ready to build your OCR app!** 🚀
