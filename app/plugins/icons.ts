import {
  AlertCircle, ArrowLeft, ArrowRight, ArrowUpRight, Award, BadgeCheck, BarChart3,
  BookOpen, Briefcase, Building2, Bus, Calendar, Check, CheckCircle2, ChevronDown,
  ChevronUp, CircleCheck, CircleDot, Clock, CloudCog, Code2, Compass, Database, Download,
  ExternalLink, Eye, EyeOff, FileText, Filter, Gauge, Globe, GraduationCap, Headphones,
  HeartHandshake, HelpCircle, Home, Image, Info, KeyRound, Landmark, Layers, LayoutGrid, Lightbulb,
  LineChart, Link2, Lock, LogIn, LogOut, Mail, MapPin, Megaphone, Menu, MessageCircle,
  Mic, MonitorSmartphone, Network, Newspaper, Paperclip, PenLine, Phone, PieChart, Play,
  Plus, Minus, Quote, Rocket, Scale, Search, Send, Server, Settings, Shield, ShieldCheck,
  SlidersHorizontal, Sparkles, Star, Target, Timer, TrendingUp, UserRound, Users, Video,
  Wallet, Workflow, X, Zap
} from '@lucide/vue'

// Register Lucide icons globally so every page can use <Check />, <ArrowRight />
// etc. without per-file imports. Zero emoji/glyph characters in templates.
const icons: Record<string, unknown> = {
  AlertCircle, ArrowLeft, ArrowRight, ArrowUpRight, Award, BadgeCheck, BarChart3,
  BookOpen, Briefcase, Building2, Bus, Calendar, Check, CheckCircle2, ChevronDown,
  ChevronUp, CircleCheck, CircleDot, Clock, CloudCog, Code2, Compass, Database, Download,
  ExternalLink, Eye, EyeOff, FileText, Filter, Gauge, Globe, GraduationCap, Headphones,
  HeartHandshake, HelpCircle, Home, Image, Info, KeyRound, Landmark, Layers, LayoutGrid, Lightbulb,
  LineChart, Link2, Lock, LogIn, LogOut, Mail, MapPin, Megaphone, Menu, MessageCircle,
  Mic, MonitorSmartphone, Network, Newspaper, Paperclip, PenLine, Phone, PieChart, Play,
  Plus, Minus, Quote, Rocket, Scale, Search, Send, Server, Settings, Shield, ShieldCheck,
  SlidersHorizontal, Sparkles, Star, Target, Timer, TrendingUp, UserRound, Users, Video,
  Wallet, Workflow, X, Zap
}

export default defineNuxtPlugin((nuxtApp) => {
  for (const [name, component] of Object.entries(icons)) {
    nuxtApp.vueApp.component(name, component as never)
  }
})
