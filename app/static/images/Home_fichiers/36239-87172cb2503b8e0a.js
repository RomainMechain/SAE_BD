"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[36239],{4784:function(e,n,t){t.d(n,{k:function(){return c}});var o=function(e){var n=e.musicSubscriptions,t=e.flexSubscriptions,o=n&&(null==n?void 0:n.length)<1||(null==n?void 0:n.length)===void 0,a=t&&(null==t?void 0:t.length)<1||(null==t?void 0:t.length)===void 0;return o&&a?{userHasPremiumMusicSub:!1,userHasMusicSubs:!1,userHasFlexSub:!1}:{userHasPremiumMusicSub:Boolean(n.find(function(e){var n;return/music_premium/g.test(null==e?void 0:null===(n=e.product)||void 0===n?void 0:n.name)})||!1),userHasMusicSubs:!o,userHasFlexSub:!a}},a=t(8149),i=t(95902),s=t(65532),r=t(44297),l=t(62767),c=function(e){var n=e.asset,t=(0,s.PE)().region,c=(0,l.av)().data,d=o(c||{musicSubscriptions:[],flexSubscriptions:[]}),u=d.userHasPremiumMusicSub,p=d.userHasFlexSub,m=d.userHasMusicSubs,h=(0,r.O)({track:n,useContentTier:!0})||!1,f=t===i.g7;return(null==n?void 0:n.type)!==a.jr||f||u||!c||p?{showMusicConversionPanel:!1,isLoading:!c}:h?{showMusicConversionPanel:(!u||!m)&&!p,isLoading:!c}:{showMusicConversionPanel:!m&&!p,isLoading:!c}}},33962:function(e,n,t){t.d(n,{i:function(){return e6}});var o=t(70865),a=t(96670),i=t(50930),s=t(52322),r=t(72841),l=t(47842),c=t(83415),d=t(41075),u=t(62197),p=t(79441),m=t(65532),h=t(26051),f=t(44297),b=t(87394),g=t(2784),v=t(19819),C=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},n=e.threshold,t=void 0===n?1/0:n,o=e.skip,a=void 0!==o&&o,i=e.initialStateValue,s=(0,b.Z)((0,g.useState)(void 0!==i&&i),2),r=s[0],l=s[1];return(0,g.useEffect)(function(){if(!a){var e=(0,v.Zc)(function(){window.pageYOffset>=t?l(!0):l(!1)});return window.addEventListener("scroll",e,{passive:!0}),function(){return e&&window.removeEventListener("scroll",e)}}},[t,a]),r},x=t(8655),w=t(43822),y=t(58487),k=t(94909),L=t(81166),Z=t(8740),j=t(26297),A=t(67550),B=(0,Z.ZL)()(function(e,n){var t,o=e.palette,a=e.typography,i=e.breakpoints,s=e.tokens.spacing,r=n.bgColor,c=n.textColor;return{topNav:(0,l.Z)({display:"flex",width:"100%",zIndex:2,height:"".concat(87,"px"),boxShadow:"0px 16px 48px rgba(0, 0, 0, 12%)"},i.down("sm"),{display:"none"}),topNavFixed:{zIndex:10,position:"fixed",top:0,left:0,backgroundColor:r},root:(0,l.Z)({display:"flex",justifyContent:"space-between",width:"100%",margin:"0 auto",maxWidth:i.values.lg,padding:"0 ".concat(s.m)},i.up("md"),{padding:"0 ".concat(s.m," 0 ").concat(s["3xl"])}),assetDescriptionPortrait:{paddingLeft:"60px"},assetDescriptionLandscape:{paddingLeft:"90px"},assetDescription:{margin:"20px 0",paddingTop:"5px",position:"relative",overflow:"hidden"},actionButtons:(0,l.Z)({marginTop:"10px"},i.down("md"),{marginTop:0}),icon:{position:"absolute",top:0,left:0,zIndex:1},iconPortrait:{width:"40px"},iconLandscape:{width:"75px"},title:{whiteSpace:"nowrap",fontSize:"12px",fontWeight:700,color:c},type:{fontSize:"12px",color:c},buttonVariantFilter:{color:c,display:"block",width:"100%",height:"100%",backgroundColor:"inherit",border:0,minWidth:0,lineHeight:1.3,fontWeight:"normal",textAlign:"center",padding:"8px","&:hover":{border:0,backgroundColor:"inherit"}},buttonAnchor:(t={height:"auto",padding:0,minWidth:0,display:"inline-flex",fontWeight:a.fontWeightRegular,color:o.info.main},(0,l.Z)(t,i.up("sm"),{"&:hover":{backgroundColor:"inherit",color:o.text.primary},"&:focus":{backgroundColor:"inherit",color:o.text.primary}}),(0,l.Z)(t,"& .MuiTouchRipple-root",{display:"none"}),t),actionVariantRoot:(0,l.Z)({padding:s.s},i.up("md"),{padding:s.base,marginLeft:s.base}),startIcon:{margin:0}}}),I=t(47999),S=t(59481),P=t(81034),T=t(9823),D=t(776),N=(0,Z.ZL)()(function(e){var n,t=e.breakpoints,o=e.palette,a=e.tokens,i=a.spacing,s=a.fontSize;return{root:(n={color:o.info.main,display:"flex",marginTop:i.s},(0,l.Z)(n,t.up("sm"),{marginTop:i.base}),(0,l.Z)(n,"& > *:not(:first-of-type)",(0,l.Z)({marginLeft:i.s},t.up("md"),{marginLeft:i.base})),n),buttonWrapper:{display:"flex"},buttonProgress:{position:"absolute"},actionLabel:(0,l.Z)({},t.down("md"),{display:"none"}),iconSizeMedium:{"& > *:first-of-type":(0,l.Z)({},t.down("md"),{fontSize:s.icon})},startIcon:(0,l.Z)({},t.down("md"),{margin:0})}}),_=function(e){var n=e.hasIcon,t=e.withActionLabel;return n&&t?"contained":t?"text":void 0},M=function(e){var n=e.Icon,t=e.withActionLabel,o=!!n;return{color:o?"primary":"inherit",variant:_({hasIcon:o,withActionLabel:t}),startIcon:t?n:void 0,size:t?"medium":"small"}},z=function(e){var n=e.classesProps,t=e.buttons,i=e.withActionLabel,c=e.color,d=N(),u=d.classes,p=d.cx,m=B({color:c}).classes,h=i?I.z:S.h,f=(0,T.D)().isBrandSstk;return(0,s.jsx)(D.Mp,{value:P.Bh8,children:(0,s.jsx)(A.Z,{className:p(u.root,n.rootContainer),children:t.map(function(e){var t,c=e.label,d=e.href,b=e.onClick,g=e.isLoading,v=e.disabled,C=e.show,x=e.Icon,w=e.clickAnalyticsLabel,y=(0,j.Z)(e,["label","href","onClick","isLoading","disabled","show","Icon","clickAnalyticsLabel"]);return(void 0===C||C)&&(0,s.jsx)(A.Z,{className:u.buttonWrapper,children:(0,s.jsx)(h,(0,a.Z)((0,o.Z)({classes:{root:n.buttonRoot,iconSizeMedium:u.iconSizeMedium,startIcon:m.startIcon},className:p((t={},(0,l.Z)(t,m.buttonAnchor,!x),(0,l.Z)(t,m.buttonVariantFilter,!!x),t)),onClick:b,href:d,disabled:g||v,"aria-label":c,labelTrack:f?w:c},M({Icon:x,withActionLabel:i}),y),{children:i?(0,s.jsxs)(s.Fragment,{children:[g&&(0,s.jsx)(r.Z,{color:"inherit",size:18,className:u.buttonProgress}),(0,s.jsx)("span",{className:u.actionLabel,children:c})]}):x}))},c)})})})};z.defaultProps={classesProps:{},withActionLabel:!0};var F=t(83249),E=t(85801),R=(0,Z.ZL)()(function(e){var n=e.breakpoints,t=e.tokens,o=t.spacing,a=t.fontSize;return{actionRoot:(0,l.Z)({padding:o.s},n.up("md"),{padding:o.base,marginLeft:o.base}),actionLabel:(0,l.Z)({},n.down("md"),{display:"none"}),iconSizeMedium:{"& > *:first-of-type":(0,l.Z)({},n.down("md"),{fontSize:a.icon})},startIcon:(0,l.Z)({},n.down("md"),{margin:0})}}),V=function(e){var n=e.buttonProps,t=e.IconComponent,i=e.labels,r=B({color:e.color}).classes,l=R(),c=l.classes,d=l.cx;return(0,s.jsx)(F.Z,(0,a.Z)((0,o.Z)({},n),{classes:{root:r.actionVariantRoot,iconSizeMedium:c.iconSizeMedium,startIcon:r.startIcon},className:d(r.buttonVariantFilter,n.className),color:"primary",variant:"contained",startIcon:(0,s.jsx)(t,{}),children:(0,s.jsx)("span",{className:c.actionLabel,children:i.share})}))},H=function(e){var n=e.buttonProps,t=e.IconComponent,i=B({isVariant:e.isVariant}).classes,r=R(),l=r.classes,c=r.cx;return(0,s.jsx)(E.Z,(0,a.Z)((0,o.Z)({},n),{classes:{root:c(l.actionRoot,n.className)},className:i.buttonVariantFilter,color:"primary",size:"small",children:(0,s.jsx)(t,{})}))},O=t(98788),W=t(45680),U=t(68052),G=t(44417),J=t(44699),K=t(73572),Q=t(37546),q=t(48433),X=t(54112),Y=t(78809),$=t(96109),ee=t(9694),en=t(75724),et=t(1774),eo=t(34273),ea=t.n(eo),ei=t(70314),es=t.n(ei),er=t(25237),el=t.n(er),ec=es()().publicRuntimeConfig.shutterstockBaseUrl,ed=el()(function(){return t.e(51935).then(t.bind(t,51935)).then(function(e){return e.DynamicMenuDropdownContent})},{loadableGenerated:{webpack:function(){return[51935]}},ssr:!1}),eu="action-menu",ep=function(e){var n=e.asset,t=e.labels,o=e.onCloseHandler,a=e.productSharedAnalyticsEvent,i=e.shareLink,s=e.shouldTrackAnalytics,r=e.twitterCopy,l=e.setCopyLinkStatus,c=e.pageSection;return[{label:K.vq,Icon:ee.s,href:"https://www.facebook.com/sharer/sharer.php?u=".concat(encodeURIComponent(i)),isLink:!0,hasDivider:!1,onClick:function(){s&&a({asset:n,shareVia:K.vq,pageSection:c}),o()}},{label:K.Ib,Icon:en.t,href:"https://twitter.com/intent/tweet?url=".concat(encodeURIComponent(i),"&text=").concat(void 0===r?"":r),isLink:!0,hasDivider:!1,onClick:function(){s&&a({asset:n,shareVia:K.Ib,pageSection:c}),o()}},{label:t.copy,Icon:et.C,isLink:!1,onClick:(0,O.Z)(function(){var e;return(0,W.__generator)(this,function(t){switch(t.label){case 0:return t.trys.push([0,2,3,4]),[4,ea()(i)];case 1:return t.sent(),s&&a({asset:n,shareVia:"copyLink",pageSection:c}),l({status:J.MR,error:void 0}),[3,4];case 2:return e=t.sent(),l({status:J.pn,error:e}),[3,4];case 3:return o(),[7];case 4:return[2]}})}),hasDivider:!0}]},em={share:"common:actions_share",email:"account:profile_email",copy:"common:actions_copy",copyToClipBoardSuccess:"developers:apps_copied_to_clipboard",copyToClipBoardWarning:"notifications:label_generic_failure"},eh=function(e){var n=e.asset,t=e.ButtonComponent,i=e.classes,r=e.IconComponent,l=e.hasTooltip,c=e.iconContainerClassName,d=e.shouldTrackAnalytics,u=e.clickAnalyticsLabel,p=e.size,m=e.color,h=(0,D.yh)().analytics,f=u.pageSection,v=u.eventLabel,C=(0,X.D)({namespace:U.VQ6,translationKeys:em}).labels,x=n.type,w=n.description,y=(0,Y.M)(),k=(0,Q.Lr)(n),L=(0,b.Z)((0,$.r)((0,a.Z)((0,o.Z)({},k),{assetType:x,slug:y({description:w})})),1)[0],Z=(0,b.Z)((0,g.useState)(null),2),j=Z[0],A=Z[1],B=(0,b.Z)((0,g.useState)(!1),2),I=B[0],S=B[1],T=(0,b.Z)((0,g.useState)({status:"",error:void 0}),2),N=T[0],_=T[1],M=(0,q.W)(),z=function(){I||S(!0)},F=function(e){z(),A(e)},E=function(){return F(null)},R=ep({asset:n,labels:C,onCloseHandler:E,productSharedAnalyticsEvent:M,setCopyLinkStatus:_,shareLink:"".concat(ec).concat(L),shouldTrackAnalytics:d,twitterCopy:w,pageSection:P.df}),V=(0,a.Z)((0,o.Z)({size:p,"aria-label":C.share},I&&j&&{"aria-controls":eu}),{"aria-haspopup":"true",className:i.button,onClick:function(e){d&&h.click({pageSection:f||P.hTM,eventLabel:v||P.$cX}),F(e.currentTarget)},onMouseEnter:z});return(0,s.jsxs)("div",{className:c,children:[(0,s.jsx)(t,{IconComponent:r,buttonProps:V,labels:C,color:m,hasTooltip:l}),I&&(0,s.jsx)(ed,{id:eu,anchorEl:j,menuOptions:R,onCloseHandler:E}),(0,s.jsx)(G.Y,{alertSeverity:N.status,error:N.error,handleSnackbarClose:function(){return _({status:""})},isOpen:!!N.status,message:N.status===J.MR?C.copyToClipBoardSuccess:C.copyToClipBoardWarning})]})};eh.defaultProps={classes:{},clickAnalyticsLabel:{},hasTooltip:!1,shouldTrackAnalytics:!1,IconComponent:L.m,size:"small"};var ef=(0,Z.ZL)()(function(e,n){var t,a,i=e.breakpoints,s=e.tokens,r=s.size,c=s.spacing,d=n.flexBreakpoint,u=n.isCentered;return{root:(0,o.Z)({display:"flex",flexDirection:"column",justifyContent:"center",marginTop:c.base,minHeight:r.density.high},"md"===d?(0,l.Z)({},i.up("md"),{marginTop:0,flexDirection:"row"}):(t={},(0,l.Z)(t,i.up("md"),{marginTop:0,marginBottom:c.base}),(0,l.Z)(t,i.up(d),{flexDirection:"row"}),t)),container:(0,o.Z)({width:"100%"},u&&(0,l.Z)({},i.up("md"),{width:"auto"})),ctas:(0,o.Z)({color:"#FFFFFF",alignItems:"center"},"md"===d?(0,l.Z)({},i.up("md"),{marginLeft:c.base,display:"flex",justifyContent:"flex-end"}):(a={},(0,l.Z)(a,i.up(d),{marginLeft:c.s,display:"flex",justifyContent:"flex-end"}),(0,l.Z)(a,i.up("md"),{marginLeft:c.base}),a)),channelBanner:{marginRight:c.s},actionButtonRoot:(0,l.Z)({padding:c.s,marginBottom:0},i.up("md"),{padding:c.base}),actionIcons:{display:"flex",width:"auto"},actionRootContainer:{marginTop:0,alignItems:"center",display:"flex"},shareButtonContainer:(0,l.Z)({display:"flex",alignItems:"center"},i.down("md"),{marginLeft:c.s}),banner:(0,l.Z)({width:"100%",display:"flex",justifyContent:"space-between",marginBottom:c.s},i.up("sm"),{marginBottom:0})}}),eb=function(e){var n=e.asset,t=e.flexBreakpoint,a=e.clickAnalyticsLabels,i=e.CtaComponent,r=e.actionButtons,l=e.showShareButton,c=e.ctaComponentProps,d=e.isCentered,u=e.color,p=e.disableChannelBanner,m=ef({flexBreakpoint:t,isCentered:d}),h=m.classes,f=m.cx,b=!(0,k.d)({breakpoint:"sm"}),g=(null==r?void 0:r.length)||l;return(0,s.jsxs)("div",{className:f(h.root,h.container),children:[(!p||g)&&(0,s.jsxs)("div",{className:h.banner,children:[!p&&(0,s.jsx)(y.h,{classes:{root:h.channelBanner},asset:n,withLabel:!1}),g&&(0,s.jsxs)("div",{className:h.actionIcons,children:[r&&(0,s.jsx)(z,{classesProps:{rootContainer:h.actionRootContainer},buttons:r,withActionLabel:b,color:u}),l&&(0,s.jsx)(eh,{asset:n,IconComponent:L.m,ButtonComponent:b?V:H,clickAnalyticsLabel:a.shareButton,iconContainerClassName:h.shareButtonContainer,shouldTrackAnalytics:!0,size:"medium",color:u})]})]}),i&&(0,s.jsx)("div",{className:h.ctas,children:(0,s.jsx)(i,(0,o.Z)({asset:n},c))})]})};eb.defaultProps={flexBreakpoint:"sm",actionButtons:null,CtaComponent:null,ctaComponentProps:{},isCentered:!1,clickAnalyticsLabels:""};var eg=function(e){var n,t,o=e.actionButtons,a=e.asset,i=e.clickAnalyticsLabels,r=e.CtaComponent,b=e.ctaComponentProps,g=e.showShareButton,v=e.disableChannelBanner,y=(0,m.PE)().locale,k=(0,p.L)({asset:a}).showLoggedOutConversionPanel,L=(0,x.g)({asset:a}).showImageConversionPanel,Z="#ffffff",j=a.aspect<1?"portrait":"landscape",A=(0,f.Am)(a),I=(0,h.G)({asset:a,language:y}),S=C({threshold:k||L?625:220,skip:(null==document?void 0:null===(n=document.documentElement)||void 0===n?void 0:n.clientWidth)<=w.w.breakpoints.values.sm}),P=B({bgColor:"#232835",textColor:Z}),T=P.classes,D=P.cx,N={portrait:T.assetDescriptionPortrait,landscape:T.assetDescriptionLandscape},_={portrait:T.iconPortrait,landscape:T.iconLandscape};return(0,s.jsx)(s.Fragment,{children:S&&(0,s.jsx)(c.Z,{direction:"down",in:S,children:(0,s.jsx)("div",{id:"top-nav-banner",className:D(T.topNav,(0,l.Z)({},T.topNavFixed,S)),children:(0,s.jsxs)(d.ZP,{className:T.root,children:[(0,s.jsxs)(d.ZP,{className:D(T.assetDescription,N[j]),children:[(0,s.jsx)("img",{className:D(T.icon,_[j]),src:A?a.previewImageUrl:a.src,alt:null!==(t=a.alt)&&void 0!==t?t:I}),(0,s.jsx)(u.Z,{className:T.title,children:A?I:a.title}),(0,s.jsx)(u.Z,{className:T.type,children:a.type})]}),(0,s.jsx)(d.ZP,{className:T.actionButtons,children:(0,s.jsx)(eb,{actionButtons:o,asset:a,clickAnalyticsLabels:i,CtaComponent:r,ctaComponentProps:b,isCentered:!0,showShareButton:g,color:Z,disableChannelBanner:void 0!==v&&v})})]})})})})},ev=t(80837),eC=t(98202),ex=t(9390),ew=t(91609),ey=t(73377),ek=t(17411),eL=t(59877),eZ=ex.r,ej=(0,Z.ZL)()(function(){var e,n,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},o=t.breakpoints,a=t.palette,i=t.tokens,s=i.color,r=i.size,c=i.spacing,d=a.mode===ew.oc.DARK,u=d?s["white-96"]:s.gray["onyx-87"],p=d?a.common.black:a.common.white;return{root:(e={display:"flex",flexDirection:"column",justifyContent:"center",alignItems:"flex-start",marginTop:c.base,minHeight:r.density.high},(0,l.Z)(e,o.down("md"),{alignItems:"normal",flexWrap:"wrap"}),(0,l.Z)(e,o.up("md"),{marginTop:0,marginBottom:c.base,alignItems:"flex-start"}),(0,l.Z)(e,o.up("sm"),{flexDirection:"row"}),e),container:{width:"100%"},buttonProgress:{position:"absolute"},ctas:(n={alignItems:"center"},(0,l.Z)(n,o.up("sm"),{marginLeft:c.s,display:"flex",justifyContent:"flex-end"}),(0,l.Z)(n,o.up("md"),{marginLeft:c.base}),n),tooltip:{"&&":{color:p,backgroundColor:u}},tooltipContent:{display:"inline",cursor:"default"},banner:{width:"80%",display:"flex",justifyContent:"space-around",marginBottom:c.s},textLink:{color:a.info.main,"&:hover":{color:a.text.primary}}}}),eA=el()(function(){return t.e(97415).then(t.bind(t,97415))},{loadableGenerated:{webpack:function(){return[97415]}},ssr:!1}),eB=function(e){var n,t=e.assetDownloadUrl,o=e.showDescription,a=e.color,i=e.variant,l=e.clickAnalyticsLabels,c=ej(),d=c.classes,u=c.cx,p=(0,b.Z)((0,g.useState)(!1),2),m=p[0],h=p[1],f=(n=(0,O.Z)(function(){return(0,W.__generator)(this,function(e){switch(e.label){case 0:if(!t||m)return[2];return h(!0),[4,(0,ek.S)(t)];case 1:return e.sent(),h(!1),[2]}})}),function(){return n.apply(this,arguments)}),v=l.dreamDownloadForFreeButton,C=l.dreamLearnMoreButton,x=(0,X.D)({namespace:U.Otp,translationKeys:{downloadForFree:"image:logout_adp_free_trial_download",standardLicenseDescription:"comparison_table_licenses_section:feature1:description",learnMore:"pricing_card_learn_more"}}),w=x.t,y=x.labels;return(0,s.jsxs)("div",{className:u(d.root,d.container),children:[o&&(0,s.jsx)("div",{className:d.banner,children:(0,s.jsxs)("span",{children:[(0,s.jsx)(eL.cC,{ns:U.Otp,i18nKey:"dream_campaign:free_download_description",components:{b:(0,s.jsx)("b",{}),i:(0,s.jsx)("i",{})},t:w}),"\xa0",(0,s.jsx)(eA,{disableInteractive:!0,title:(0,s.jsx)("span",{className:d.tooltipContent,children:y.standardLicenseDescription}),children:(0,s.jsxs)(eZ,{href:"/explore/dream",underline:!0,className:d.textLink,clickAnalyticsLabel:(0,ey.U_)(C),children:[y.learnMore,"."]})})]})}),(0,s.jsx)("div",{className:d.ctas,children:(0,s.jsxs)(I.z,{color:a,variant:i,disabled:m,fullWidth:!0,onClick:f,clickTrack:(0,ey.U_)(v),"aria-label":y.downloadForFree,children:[m&&(0,s.jsx)(r.Z,{size:24,color:"inherit",className:d.buttonProgress}),y.downloadForFree]})})]})};eB.defaultProps={assetDownloadUrl:null,showDescription:!1,color:"secondary",variant:"contained"};var eI=t(79866),eS=t(4784),eP=t(11265),eT=t(37211),eD=t(8149),eN=t(80073),e_=t(15090),eM=t(14017),ez=t(29292),eF=t(449),eE=t(84866),eR=function(e){var n;return(null==e?void 0:null===(n=e.contributor)||void 0===n?void 0:n.id)&&(0,eE.n_)({contributorId:e.contributor.id})?{downloadUrl:(0,eE.bI)(e)}:{}},eV=t(17604),eH=t(52309),eO=t(65094),eW=t(31037),eU=t(80672),eG=t(32545),eJ=t(68034),eK=t(90154),eQ=t(66832),eq=t(79454),eX=t(86097),eY=t(5632),e$=t(43637),e0=t(70008),e1=t(12649),e4=function(e){var n=e.asset,t=(0,e1.B)(),o=(0,k.d)(),a=(0,e0.B)().isIndiaRegion,i=(0,f.aT)(n),s=(0,f.f8)(n),r=(0,f.PD)(n),l=(0,e$.k7)(n),c=(0,f.N3)(n);return{shouldRenderSDAQ336:!t&&i&&!c&&!s&&!r&&!l&&o&&!a}},e2=t(62767),e7=function(e){var n=e.asset,t=(0,k.d)(),o=(0,e2.V9)().data,a=(void 0===o?{}:o).totalNumSubscriptionsActive,i=(0,f.aT)(n)&&!(0,f.N3)(n),s=(0,f.PD)({channels:null==n?void 0:n.channels}),r=(0,f.f8)(n);return(0===a||void 0===a)&&!t&&i&&!s&&!r},e3=el()(function(){return t.e(40117).then(t.bind(t,31360)).then(function(e){return e.ExperimentSDAQ336})},{loadableGenerated:{webpack:function(){return[31360]}},ssr:!0}),e9=el()(function(){return t.e(41102).then(t.bind(t,10222)).then(function(e){return e.ExperimentAssetDownloadCta})},{loadableGenerated:{webpack:function(){return[10222]}},ssr:!0}),e6=function(e){var n=e.addToCollectionViewsHandler,t=e.asset,l=e.canOpenDrawerOnLoad,c=e.clickAnalyticsLabels,d=e.labels,u=e.redirectToCollectionDetailsPage,p=e.isTemplateAsset,m=e.isPaidUserConversionPanel,h=(0,eY.useRouter)().asPath,b=(0,eV.t)({asset:t,isTemplateAsset:p,labels:d}),v=b.editorButtonHref,C=b.editorButtonLabel,w=b.isCreate,y=b.onClick,k=c.addToCollections,L=c.editButton,Z=c.tryButton,j=(0,eF.i)({asset:t,clickAnalyticsLabels:c}),A=j.tryButtonClickHandler,B=j.isActionInProgress,I=j.isMusicPreviewModalOpen,S=j.setIsMusicPreviewModalOpen,T=j.isSignUpModalOpen,D=j.setIsSignUpModalOpen,N=eR(t).downloadUrl,_=(0,eH.B)(I),M=(0,eO.E)({asset:t}),z=M.showSaveButton,F=M.showShareButton,E=M.showEditButton,R=M.showTryButton,V=M.showDownloadForFreeButton,H=M.showGenerateActionButtons,O=(0,x.g)({asset:t}),W=O.showImageConversionPanel,U=O.isLoading,G=e4({asset:t}).shouldRenderSDAQ336,J=(0,eM.g)({asset:t}).isEligibleForCVRT1633,K=e7({asset:t}),Q=(0,f.aT)(t)&&!(0,f.N3)(t),q=(0,f.Am)(t)&&!(0,f.so)(t),X=(0,f.PD)({channels:null==t?void 0:t.channels}),Y=(0,g.useMemo)(function(){return(0,i.Z)(z?[(0,o.Z)({label:d.save,onClick:function(){n({assets:[t],gridItems:[],redirectToCollectionDetailsPage:u,openModal:!0})},rel:"nofollow",Icon:(0,s.jsx)(eJ.X,{}),clickAnalyticsLabel:null==k?void 0:k.eventLabel},X&&{brandCategory:(0,ez.f_)(t),productLine:(0,ez.Rz)(t)})]:[]).concat((0,i.Z)(R?[(0,o.Z)({label:d.try,onClick:function(){A()},rel:"nofollow",Icon:B?(0,s.jsx)(r.Z,{size:20}):(0,s.jsx)(eK.I,{}),clickAnalyticsLabel:null==Z?void 0:Z.eventLabel,"data-optimize":"download-watermark-cta"},X&&{brandCategory:(0,ez.f_)(t),productLine:(0,ez.Rz)(t)})]:[]),(0,i.Z)(E?[(0,a.Z)((0,o.Z)({label:C},w?{onClick:y}:{href:v}),{Icon:(0,s.jsx)(eQ.M,{}),clickAnalyticsLabel:null==L?void 0:L.eventLabel,rel:"nofollow",target:"_blank","data-automation":"edit-button-cta"})]:[]),(0,i.Z)(H?[{clickAnalyticsLabel:P.VtA,label:d.variations,Icon:(0,s.jsx)(eq.b,{}),href:(0,eW.jq)({assetId:t.id,sourceAssetType:eU.J1.Creative})[0],rel:"nofollow",dataAutomation:"ActionButton_VariationsCreativeImagesButton"},{clickAnalyticsLabel:P.ScC,label:d.expand,Icon:(0,s.jsx)(eX.H,{}),href:(0,eW.U7)({assetId:t.id,sourceAssetType:eU.J1.Creative})[0],rel:"nofollow",dataAutomation:"ActionButton_ZoomOutCreativeImagesButton"}]:[]))},[z,d.save,d.try,d.variations,d.expand,null==k?void 0:k.eventLabel,X,t,R,B,null==Z?void 0:Z.eventLabel,E,H,n,u,A,C,w,y,v,null==L?void 0:L.eventLabel]),$=W||U?function(){return(0,s.jsx)(s.Fragment,{})}:ev.i,ee=V?eB:ev.i,en=(0,eS.k)({asset:t}),et=en.showMusicConversionPanel,eo=en.isLoading,ea=(0,eG.iP)(null==t?void 0:t.holding),ei=(0,eC.A)({asset:t,clickAnalyticsLabels:c,labels:d,assetIsLicensed:ea,shouldFetchEligibility:!ea}).hasExistingLicense;(et&&!ei||m)&&($=null),G&&($=e3),J&&($=e9);var es=(0,e_.x)({asset:t}).isEligibleForExperimentCVRT1549?eN.a:eI.e;return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(eT.SignUpModal,{modalIsOpen:T,handleClose:function(){D(!1)}}),V&&(0,s.jsx)(eB,{showDescription:!0,assetDownloadUrl:N,canOpenDrawerOnLoad:l,clickAnalyticsLabels:c}),!V&&(0,s.jsx)(es,{actionButtons:Y,asset:t,clickAnalyticsLabels:c,ctaComponentProps:{asset:t,canOpenDrawerOnLoad:l,clickAnalyticsLabels:c,hideConditionsAreLoading:(null==t?void 0:t.type)===eD.jr&&eo,hideCtaComponent:X},isCentered:!0,showShareButton:F,hideCtaComponent:X,isTemplateAsset:p,CtaComponent:$}),(Q||q)&&!p&&!K&&(0,s.jsx)(eg,(0,o.Z)({},{actionButtons:Y,asset:t,clickAnalyticsLabels:c,disableChannelBanner:V,CtaComponent:ee,ctaComponentProps:{asset:t,assetDownloadUrl:N,showDescription:!1,campaignAssetDownloadURL:N,clickAnalyticsLabels:c,isScrollCTABar:!0},showShareButton:F,key:h})),_&&(0,s.jsx)(eP.D,{setIsDialogActive:S,isOpen:I,track:t})]})};e6.defaultProps={addToCollectionViewsHandler:null,asset:{},clickAnalyticsLabels:{},isTemplateAsset:!1,isPaidUserConversionPanel:!1}},38237:function(e,n,t){t.d(n,{Rf:function(){return o},S7:function(){return a},sK:function(){return i}});var o="premium",a="select",i="call_for_price"},14017:function(e,n,t){t.d(n,{g:function(){return r}});var o=t(44297),a=t(9823),i=t(12649),s=t(62767),r=function(e){var n=e.asset,t=(0,i.B)(),r=(0,a.D)().isBrandSstk,l=(0,o.Am)(n)&&!(0,o.so)(n),c=(0,s.V9)().data,d=(void 0===c?{}:c).totalNumSubscriptionsActive;return{isEligibleForCVRT1633:r&&l&&(!t||0===d)}}},17604:function(e,n,t){t.d(n,{t:function(){return b}});var o=t(16555),a=t(33301),i=t(43801),s=t(44297),r=t(9823),l=t(92405),c=t(48726),d=t(38204),u=t(5632),p=t(2784),m=t(23770),h=t(12847),f=t(19767),b=function(e){var n,b,g=e.asset,v=e.isTemplateAsset,C=e.labels,x=(0,r.D)().isBrandSstk,w=(0,i.v)(),y=(0,u.useRouter)(),k=!!(0,l.p)(a.Si,!0,!1,!0)&&x,L=(0,c.E)((0,d.$3)(g.id)),Z=(0,f.f)(g.id,{},(0,s.Tp)(g)),j=(0,c.E)(Z),A=(0,o.aL)(),B=(0,c.E)(A({templateId:g.id})),I=C.editWithCreate,S=(0,h.rE)(C.openInCreate,m.T)?C.edit:C.openInCreate;v?(n=B,b=C.edit):(n=k?j:L,b=k?S:C.edit);var P=(0,p.useCallback)(function(){var e;(null==g?void 0:null===(e=g.sizes)||void 0===e?void 0:e.hugeJpg)&&!v&&(null==w?void 0:w.current)&&Object.keys(null==w?void 0:w.current).length>0?w.current.isPeacock&&w.current.openCreateWithEdits?w.current.openCreateWithEdits(g.sizes.hugeJpg,y.locale):Promise.all([t.e(54280),t.e(48834),t.e(46194),t.e(22673)]).then(t.bind(t,16609)).then(function(e){(0,e.openCreateWithEdits)(w,g.sizes.hugeJpg,y.locale)}):window.open(n,"_blank")},[g,w,n,y.locale,v]);return{editorButtonHref:n,editorButtonLabel:b,isCreate:k,onClick:P,editWithCreateLabel:I}}},70008:function(e,n,t){t.d(n,{B:function(){return a}});var o=t(65532),a=function(){return{isIndiaRegion:"IN"===(0,o.PE)().region}}},8655:function(e,n,t){t.d(n,{g:function(){return r}});var o=t(44297),a=t(95775),i=t(94909),s=t(12649),r=function(e){var n,t,r=e.asset,l=(0,s.B)(),c=(0,i.d)(),d=(0,a.IP)({assets:[r]}),u=d.data,p=d.isLoading,m=(0,o.aT)(r)&&!(0,o.N3)(r),h=(null==u?void 0:null===(n=u.subscriptions)||void 0===n?void 0:n.length)>0,f=(null==u?void 0:null===(t=u.licenses)||void 0===t?void 0:t.length)>0;return{showImageConversionPanel:m&&!h&&u&&!f&&!c&&l,isLoading:p}}}}]);
//# sourceMappingURL=36239-87172cb2503b8e0a.js.map