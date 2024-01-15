"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[12374,17528],{65359:function(e,t,r){r.d(t,{b:function(){return l}});var i=r(70865),n=r(96670),a=r(87394),o=r(52322),u=r(23490),s=r(75298),c=r(2784),l=function(e){var t=e.Container,r=void 0===t?(0,c.forwardRef)(function(e,t){return(0,o.jsx)("div",(0,i.Z)({ref:t},e))}):t,l=e.Skeleton,d=e.children,m=e.intersectionOptions,f=e.skip,v=e.containerProps,h=(0,a.Z)((0,s.I)(void 0===m?{triggerOnce:!0,rootMargin:"100000px 0px 110px 0px"}:m),2),p=h[0],g=h[1],b=(0,u.N)().isGoodBot;return(0,o.jsx)(r,(0,n.Z)((0,i.Z)({ref:g},void 0===v?{}:v),{children:void 0!==f&&f||b||p?d:(0,o.jsx)(void 0===l?function(){return null}:l,{})}))}},16077:function(e,t,r){r.d(t,{y:function(){return i}});var i="Flat fee cancellation"},88692:function(e,t,r){r.d(t,{n:function(){return i}});var i="Flat fee cancellation v2"},10412:function(e,t,r){r.d(t,{AF:function(){return v},pu:function(){return f}});var i,n=r(47842),a=r(70865),o=r(96670),u=r(97258),s=r(8149),c=r(44297),l=r(97021),d=function(e){var t=e.asset,r=[];return[u.bm,u.RA,u.oB].forEach(function(e){var i,n,a,o,u;(null==t?void 0:null===(i=t.displays)||void 0===i?void 0:i[e])&&(null==t?void 0:null===(n=t.displays)||void 0===n?void 0:n[e].src)&&r.push({image:{url:null==t?void 0:null===(a=t.displays)||void 0===a?void 0:a[e].src,width:null==t?void 0:null===(o=t.displays)||void 0===o?void 0:o[e].width,height:null==t?void 0:null===(u=t.displays)||void 0===u?void 0:u[e].height}})}),0===r.length&&(null==t?void 0:t.src)&&r.push({image:{url:null==t?void 0:t.src,width:null==t?void 0:t.width,height:null==t?void 0:t.height}}),r},m=(i={},(0,n.Z)(i,s.k4,d),(0,n.Z)(i,s.Nk,d),(0,n.Z)(i,s.pX,function(e){var t,r,i,n,u=e.asset,s=u.previewImageUrl,c=(0,l.R)({asset:u});return[{image:(0,o.Z)((0,a.Z)({},c?{videoUrl:c}:{}),{url:s,width:null==u?void 0:null===(t=u.sizes)||void 0===t?void 0:null===(r=t.sdMpeg)||void 0===r?void 0:r.width,height:null==u?void 0:null===(i=u.sizes)||void 0===i?void 0:null===(n=i.sdMpeg)||void 0===n?void 0:n.height})}]}),i),f=function(e){var t=e.asset,r=(0,c.Tp)(t);if(m[r]){var i=m[r]({asset:t});if(i.length>0)return{image:(0,a.Z)({},i[0].image,i.length>1?{imageSmall:i[1].image}:{})}}return{}},v=function(e){var t=e.asset;if("boolean"==typeof t.rRated)return t.rRated;switch(t.rRated){case"0":return!1;case"1":return!0;default:return}}},97021:function(e,t,r){r.d(t,{R:function(){return a}});var i=r(44297),n=(0,r(5967).j)().shutterstockBaseUrl;function a(e){var t=e.asset,r=e.baseUrl;if(!(!t.id||(0,i.EK)(t)))return"".concat(null!=r?r:n,"/video/embed/").concat(t.id)}},17528:function(e,t,r){r.d(t,{Q:function(){return B}});var i=r(98788),n=r(47842),a=r(70865),o=r(96670),u=r(87394),s=r(45680),c=r(27739),l=r(44699),d=r(7819),m=r(43801),f=r(65532),v=r(3093),h=r(75445),p=r(23490),g=r(87414),b=function(e){var t=e.prices,r=void 0===t?{}:t,i=(0,v.O)(),n=(0,p.N)().isGoodBot,a=(0,f.PE)().currencyData.currency,o=void 0===a?h.a:a;return n?(0,g.Yy)({prices:r,localeCurrency:o}):i?(0,g.Yy)({prices:r,localeCurrency:"INR"}):(0,g.Yy)({prices:r,localeCurrency:o})},y=r(16077),F=r(88692),z=r(66970),S=r(12708),w=function(e){var t=e.couponCode,r=e.productName,i=null;return r===c.Pvj&&t===c.XdV?i=c.E65:r===c.fnR&&t===c.Q9B&&(i=c.Em3),i},C=r(44297),I=r(38419),x=r(18167),Z=r(38367),R=r(59979),N=r(70008),D=r(40233),P=r(12649),U=r(25936),k=r(24114),E=r(38204),O=r(31683),A=r(34406).env.NODE_CONFIG_ENV,M=function(){var e=(0,O.u4)()?"production":"qa";switch(A||e){case"dev":return"65021";case"qa":return"12424";case"production":return"14156";default:return"NO_ENV_DEFINED"}},_=function(){var e=(0,O.u4)()?"production":"qa";switch(A||e){case"dev":return"65035";case"qa":return"19606";case"production":return"17383";default:return"NO_ENV_DEFINED"}},T=r(21805),L=r(5632),j=r(2784),q=function(e){var t,r=e.couponCode,i=e.displayInlineCancellationFlow,o=(0,L.useRouter)(),u=(0,m.v)(),s=!!(null==u?void 0:null===(t=u.current)||void 0===t?void 0:t.isPeacock);return(0,j.useCallback)(function(e){var t,u=e.orderId,c=(0,I.DW)({language:o.locale,relativePath:(0,E.U2)({queryParams:(0,a.Z)({orderId:u},(null==o?void 0:o.query)||{},s&&{isCreativeAiOrder:"true"},r?(t={},(0,n.Z)(t,d.d9,r),(0,n.Z)(t,d.Gp,r),t):{},i&&{display:"inlineCancellationFlow"})})});o.push(c)},[r,s,o,i])},B=function(e){var t=e.products,r=e.asset,n=e.assetSize,m=e.couponCode,h=e.productId,p=e.productType,I=void 0===p?d.Cs:p,E=e.productOverride,O=e.seatCount,A=e.setCreateOrderStatus,B=void 0===A?function(){}:A,K=e.setIsInvalidCoupon,V=void 0===K?function(){}:K,H=e.vatNumber,Q=e.license,W=e.isLicenseDrawer,G=void 0!==W&&W,X=e.preset,Y=e.eligibilityData,$=void 0===Y?{}:Y,J=e.existingUserRedirectPath,ee=e.selectedShadowsOption,et=e.shouldForceAsset,er=e.subscriptionIdentifier,ei=e.cancellationReason,en=(0,f.PE)().region,ea=(0,N.B)().isIndiaRegion,eo=(0,P.jy)().data,eu=(0,U.u)().data,es=(0,P.B)(),ec=(0,u.Z)((0,j.useState)(!1),2),el=ec[0],ed=ec[1],em=(0,u.Z)((0,k.QD)(r)||[],2)[1],ef=$.eligibilityCurrency,ev=$.debitableIdentifier,eh=(0,j.useMemo)(function(){return null!=E?E:(0,a.Z)({},(0,g.$A)(t,h),O?{seatCount:O}:{})},[E,h,t,O]),ep=null==eh?void 0:eh.id,eg=(0,L.useRouter)().asPath,eb=b({prices:null==eh?void 0:eh.prices}),ey=(0,v.O)(),eF=(0,Z.Z)({shouldFetch:!!es}).data,ez=m||eh.couponCode,eS=w({couponCode:ez,productName:null==eh?void 0:eh.name}),ew=(0,R.Sl)({queryParams:(0,a.Z)({landing_page:(0,x.t)({couponCode:ez,productId:ep,vatNumber:H,seatCount:null==eh?void 0:eh.seatCount,doNotRedirect:!0,asset:ea||void 0!==et&&et?r:void 0,existingUserRedirect:J||em,license:Q})},X&&{preset:X}),signUpView:eS}),eC=(0,j.useCallback)(function(){if(window){var e,t;T.Z.set("referer_page",eg),null===(e=window.NREUM)||void 0===e||null===(t=e.addPageAction)||void 0===t||t.call(e,"UP3-1623 assign loggedOutHandler authRedirectPath to href",(0,o.Z)((0,a.Z)({},window.location||{}),{asPath:eg,authRedirectPath:ew})),window.location.href=ew}},[eg,ew]),eI=(0,S.F3)({paymentProfiles:eF}),ex=(0,j.useCallback)(function(e){var t,r,i={createTime:null==eo?void 0:eo.createTime,component:"useCreateOrder.js",errorCode:e.code,errorStatus:e.status,errorDetail:e.detail,errorMessage:e.message,errorStack:e.stack||"useCreateOrder",errorTitle:e.title,impersonatorId:eu.impersonatorId,msg:"UP1-2650 Order creation failed",organizationId:null==eo?void 0:eo.organizationId,referrerPath:window.location.pathname,referrerQuery:window.location.search,userId:null==eo?void 0:eo.id,username:null==eo?void 0:eo.username,isLicenseDrawer:G};null===(t=window.NREUM)||void 0===t||null===(r=t.noticeError)||void 0===r||r.call(t,e,i)},[eu,eo,G]),eZ=q({couponCode:ez,displayInlineCancellationFlow:[y.y,F.n].includes(ei)}),eR=(0,D.d)(),eN=(0,u.Z)((0,j.useState)({status:"",error:void 0}),2),eD=eN[0],eP=eN[1],eU=(0,j.useCallback)((0,i.Z)(function(){var e,t,i,u,m;return(0,s.__generator)(this,function(s){switch(s.label){case 0:if(s.trys.push([0,3,,4]),B({status:"",error:void 0}),eP({status:"",error:void 0}),ed(!0),ea&&c.Tj5.includes(ez))throw Error("free trial offer not available in India");if(!eF)return[3,2];return e=r?{assets:[{asset:r,selectedAssetSize:(0,z.DW)({assetType:(0,C.Tp)(r),assetSize:n})}]}:{},t=[],ei===y.y||ei===F.n?t.push({product:{id:ei===F.n?_():M(),type:"products"},cancellationReason:ei,subscriptionIdentifier:er}):(t.push((0,o.Z)((0,a.Z)({},e),{product:eh,productType:I})),null!=ei&&null!=er&&t.push({product:{id:M(),type:"products"},cancellationReason:ei,subscriptionIdentifier:er})),[4,(0,S.LV)({country:en,currency:ef||eb,paymentProfileId:null==eI?void 0:eI.paymentId,orderItems:t,selectedShadowsOption:ee,vatNumber:H,couponCode:ez,license:Q,debitableIdentifier:ev,showP32290Inr:ey})];case 1:i=s.sent().data,B({status:l.MR,error:void 0}),eP({status:l.MR,error:void 0}),ed(!1),eZ({orderId:i.id}),eR({actionName:"convert - order creation success",customAttributes:{productName:eh.name,productType:I,country:en,currency:ef||eb,assetType:(0,C.Tp)(r),assetSize:n,license:Q,isLicenseDrawer:G}}),s.label=2;case 2:return[3,4];case 3:return u=s.sent(),B({status:l.cM,error:u}),eP({status:l.cM,error:u}),ed(!1),(null==u?void 0:null===(m=u.detail)||void 0===m?void 0:m.toLowerCase())===d.LQ&&V(!0),ex(u),[3,4];case 4:return[2]}})}),[B,ea,ez,eF,r,n,en,ef,eb,null==eI?void 0:eI.paymentId,eh,I,H,Q,ev,eZ,eR,G,ex,V,ee,er,ei,ey]);return{createOrderHandler:es?eU:eC,isCreateOrderInProgress:el,product:eh,orderStatus:eD}}},38367:function(e,t,r){r.d(t,{Z:function(){return s}});var i=r(81740),n=r(49670),a=r(9009),o=r(3255),u=function(e){var t=e.queryParams;return(0,i.cF)({queryParams:t}).formattedUrl},s=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.queryParams,r=e.shouldFetch;return(0,o.ZP)(void 0===r||r?u({queryParams:void 0===t?{}:t}):null,function(e){return n.uS.get(e).then(function(e){return(0,a.O)(e.data)})})}},68769:function(e,t,r){r.d(t,{RO:function(){return T},Ch:function(){return j},It:function(){return A},Rc:function(){return P},Ux:function(){return C},kn:function(){return M},oE:function(){return I}});var i,n=r(47842),a=r(70865),o=r(96670),u=r(87394),s=r(50930),c=r(19522),l=r(8149),d=r(65537),m="kilobyte",f="megabyte",v="gigabyte",h="inch",p="centimeter",g=r(65532),b=r(37546),y=r(44297),F=r(2784),z=r(82603),S=function(){var e,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return null===(e=t.toString().match(/[0-9.,]+/))||void 0===e?void 0:e[0]},w=(i={},(0,n.Z)(i,d.xn,{suffix:"px",widthKey:"width",heightKey:"height"}),(0,n.Z)(i,d.tS,{suffix:"in",widthKey:"widthIn",heightKey:"heightIn"}),(0,n.Z)(i,d.IC,{suffix:"cm",widthKey:"widthCm",heightKey:"heightCm"}),i),C=function(e){var t=(0,g.PE)().fullLocale;return new Intl.NumberFormat(t,e).format},I=function(e){var t=e.unit,r=e.maximumFractionDigits,i=(0,u.Z)((0,F.useState)(""),2),n=i[0],a=i[1],o=(0,g.PE)().fullLocale,s=(0,F.useMemo)(function(){try{return new Intl.NumberFormat(o,{style:"unit",unit:t,maximumFractionDigits:r})}catch(e){return a(e),{format:function(e){return e}}}},[o,r,t]);return(0,F.useMemo)(function(){return{format:s.format,error:n}},[s.format,n])},x=function(e){var t=e.humanReadableSize,r=e.size,i=e.name;return t||"".concat(r.toFixed(1)," ").concat(i)},Z=function(e){var t=e.formatter,r=e.humanReadableSize,i=e.size,n=e.name,a=t.error,o=t.format;return a?x({humanReadableSize:r,size:i,name:n}):o(i)},R=function(e){var t=e.bytes,r=e.gbFormatter,i=e.mbFormatter,n=e.kbFormatter,a=e.humanReadableSize,o=t/1e3,u=o/1e3,s=u/1e3;return s>=1?Z({formatter:r,humanReadableSize:a,size:s,name:"GB"}):u>=1?Z({formatter:i,humanReadableSize:a,size:u,name:"MB"}):Z({formatter:n,humanReadableSize:a,size:o,name:"KB"})},N=function(e,t,r){var i=w[e]||{},n=i.suffix,a=i.widthKey,o=i.heightKey,s=r[e],c=(0,u.Z)([t[a],t[o]].map(function(e){return e&&Number(S(e))}),2),l=c[0],d=c[1],m=!Number.isNaN(l)&&l>0,f=!Number.isNaN(d)&&d>0;return m||f?{formattedWidth:m?Z({formatter:s,size:l,name:n}):"",formattedHeight:f?Z({formatter:s,size:d,name:n}):""}:{}},D=function(e){var t=e.assetSize,r=e.kbFormatter,i=e.mbFormatter,n=e.gbFormatter,a=t.sizeInBytes,o=t.humanReadableSize,u=t.fileSize;return a||u||o?R({bytes:a||1e3*u,gbFormatter:n,mbFormatter:i,kbFormatter:r,humanReadableSize:o}):""},P=function(e){return D({assetSize:e.assetSize,kbFormatter:I({unit:m,maximumFractionDigits:0}),mbFormatter:I({unit:f,maximumFractionDigits:1}),gbFormatter:I({unit:v,maximumFractionDigits:1})})},U=function(e){var t=e.formattedWidth,r=e.formattedHeight;return"".concat(S(t)," \xd7 ").concat(r)},k=function(e){var t,r=e.assetSize,i=e.displayUnits,a=e.inchFormatter,o=e.centimeterFormatter,u=e.labels,s=void 0===u?{}:u,c=N(i,r,(t={},(0,n.Z)(t,d.tS,a),(0,n.Z)(t,d.IC,o),(0,n.Z)(t,d.xn,{format:function(e){return s.pixels?"".concat(e," ").concat(s.pixels):"".concat(e," ").concat(w[d.xn].suffix)}}),t)),l=c.formattedWidth,m=c.formattedHeight;return l||m?U({formattedWidth:l,formattedHeight:m}):""},E=function(e){return k(e)||k((0,o.Z)((0,a.Z)({},e),{displayUnits:d.xn}))},O=function(e){var t=e.displayUnits,r=e.assetSize,i=e.inchFormatter,n=e.centimeterFormatter,a=e.labels;return t===d.xn?E({assetSize:r,displayUnits:d.tS,inchFormatter:i,centimeterFormatter:n,labels:a}):E({assetSize:r,displayUnits:t,inchFormatter:i,centimeterFormatter:n,labels:a})},A=function(e){var t=e.isImageAsset,r=e.assetSize,i=e.labels,a=(0,z.n)(),o=I({unit:h,maximumFractionDigits:0}),u=I({unit:p,maximumFractionDigits:0}),s=E({assetSize:r,displayUnits:d.xn,inchFormatter:o,centimeterFormatter:u,labels:i}),c=(0,n.Z)({},d.xn,s);return t&&(c.formattedDimensions=O({assetSize:r,labels:i,displayUnits:a,inchFormatter:o,centimeterFormatter:u})),c},M=function(){var e=(0,z.n)(),t=I({unit:m,maximumFractionDigits:0}),r=I({unit:f,maximumFractionDigits:1}),i=I({unit:v,maximumFractionDigits:1}),n=I({unit:h,maximumFractionDigits:0}),a=I({unit:p,maximumFractionDigits:0});return(0,F.useCallback)(function(o){var u=o.assetSize,s=D({assetSize:u,kbFormatter:t,mbFormatter:r,gbFormatter:i}),c=E({assetSize:u,displayUnits:e,inchFormatter:n,centimeterFormatter:a});return s?{resolutionDetails:c,size:s}:{resolutionDetails:c}},[a,e,n,i,r,t])},_=function(e){var t,r=e.assetSize,i=e.centimeterFormatter,n=e.displayUnits,a=e.inchFormatter,o=e.isImageAsset,u=e.labels,c=e.isVideoAsset,m=e.isDesignAsset,f=r.format,v=r.dpi,h=r.name,p=r.resolution,g=(null==f?void 0:f.toUpperCase())||"";if(h===l.gf)return g;var b=E({assetSize:r,PIXELS:d.xn,inchFormatter:a,centimeterFormatter:i,labels:u});return t=(o||m)&&v?[b,O({assetSize:r,labels:u,displayUnits:n,inchFormatter:a,centimeterFormatter:i}),"".concat(u.dpi," ").concat(v),g]:c?[u[null==p?void 0:p.toLowerCase()]||"",b,g]:[b,g],(0,s.Z)(new Set(t)).filter(function(e){return!!e}).join(" • ")},T=function(e){var t=e.sizes;return(void 0===t?[]:t).filter(function(e){return e.format!==c.LX})},L=function(e){var t=e.limit,r=void 0===t?0:t,i=e.sortedSizes;return r>0?null==i?void 0:i.slice(0,r):i},j=function(){var e=(0,z.n)(),t=I({unit:h,maximumFractionDigits:1}),r=I({unit:p,maximumFractionDigits:1});return(0,F.useCallback)(function(i){var n=i.asset,a=i.labels,o=i.limit,u=(0,y.aT)(n),s=(0,y.Am)(n),c=(0,y.ML)(n),l=u||c?T({sizes:Object.values(n.sizes||{})}):n.sizes,d=L({limit:void 0===o?0:o,sortedSizes:u||c?(0,b.hQ)(Object.values(l)):(0,b.Z)({sizes:l})});return{formattedSizes:null==d?void 0:d.map(function(i){return _({assetSize:i,centimeterFormatter:r,displayUnits:e,inchFormatter:t,isImageAsset:u,isDesignAsset:c,labels:a,isVideoAsset:s})})}},[e,r,t])}},33220:function(e,t,r){r.d(t,{M:function(){return o}});var i=r(27764),n=r(5632),a=/^\/search(.+)?$/,o=function(){var e=(0,n.useRouter)().asPath;return a.test((0,i.oY)(e))}}}]);
//# sourceMappingURL=12374-0e7523f3977c80a5.js.map